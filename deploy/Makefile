# Makefile für Docker-Setup im deploy-Ordner

COMPOSE = docker-compose --env-file ../.env -f docker-compose.yml
BACKUP_DIR = ../db/backup

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

logs:
	$(COMPOSE) logs -f

restart: down up

ps:
	$(COMPOSE) ps

# ----------------------------
# Einzelne Container steuern
# ----------------------------
up-db:
	$(COMPOSE) up -d db

up-web:
	$(COMPOSE) up -d web

down-db:
	$(COMPOSE) stop db

down-web:
	$(COMPOSE) stop web

restart-db: down-db up-db

restart-web: down-web up-web

# ----------------------------
# DB-Befehle
# ----------------------------
db-shell:
	docker exec -it mariadb mariadb -u$$MYSQL_USER -p$$MYSQL_PASSWORD $$MYSQL_DATABASE


#backup:
#	@mkdir -p $(BACKUP_DIR)
#	@timestamp=$$(date +"Datenbankbackup_%Y-%m-%d_%H-%M-%S.sql"); \
#	echo "Erstelle Backup $$timestamp ..."; \
#	docker exec mariadb mariadb-dump -u$$MYSQL_USER -p$$MYSQL_PASSWORD $$MYSQL_DATABASE > $(BACKUP_DIR)/$$timestamp; \
#	cp $(BACKUP_DIR)/$$timestamp $(BACKUP_DIR)/latest.sql; \
#	echo "Backup gespeichert unter $(BACKUP_DIR)/$$timestamp und aktualisiert latest.sql"; \
#	# Nur die 5 neuesten behalten
#	ls -1t $(BACKUP_DIR)/Datenbankbackup_*.sql | tail -n +6 | xargs -r rm --; \
#	echo "Ältere Backups entfernt, es bleiben maximal 5."


restore:
	@if [ -z "$(FILE)" ]; then \
		echo "Bitte Backup-Datei angeben, z. B.:"; \
		echo "  make restore FILE=$(BACKUP_DIR)/latest.sql"; \
		exit 1; \
	fi; \
	echo "Stelle Backup $(FILE) wieder her..."; \
	docker exec -i mariadb mariadb -u$$MYSQL_USER -p$$MYSQL_PASSWORD $$MYSQL_DATABASE < $(FILE); \
	echo "Restore abgeschlossen."

