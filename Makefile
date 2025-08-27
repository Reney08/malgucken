DOCKER_COMPOSE = docker-compose -f code/docker-compose.yml
PROJECT_NAME   = malgucken
DB_CONTAINER   = cocktail_db
DB_USER        = root
DB_PASSWORD    = Keins123!
DB_NAME        = BarbotDB
BACKUP_FILE    = backup/latest.sql   # relativer Pfad

.PHONY: build up down logs ps check-db import-db

build:
	$(DOCKER_COMPOSE) build

up: check-db
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

logs:
	$(DOCKER_COMPOSE) logs -f

ps:
	$(DOCKER_COMPOSE) ps

# Check ob DB-Container läuft, wenn nicht: starten + Backup einspielen
check-db:
	@if [ -z "$$(docker ps -q -f name=$(DB_CONTAINER))" ]; then \
		echo "📦 Kein laufender DB-Container gefunden, starte neuen..."; \
		$(DOCKER_COMPOSE) up -d db; \
		echo "⏳ Warte bis MariaDB bereit ist..."; \
		sleep 15; \
		$(MAKE) import-db; \
	else \
		echo "✅ MariaDB läuft bereits, kein neuer Container nötig."; \
	fi

# Backup importieren (mit mariadb-Client statt mysql!)
import-db:
	@if [ -f $(BACKUP_FILE) ]; then \
		echo "💾 Importiere Backup aus $(BACKUP_FILE)..."; \
		docker exec -i $(DB_CONTAINER) sh -c 'exec mariadb -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME)' < $(BACKUP_FILE); \
	else \
		echo "⚠️ Kein Backup gefunden unter $(BACKUP_FILE)"; \
	fi
