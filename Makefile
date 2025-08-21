PROJECT_NAME = myproject
DB_CONTAINER = mariadb
BACKUP_FILE = ./backup/latest.sql

.PHONY: up down backup restore

# Container starten + Backup einspielen
up: restore
	docker compose up -d

# Container stoppen + Backup erzeugen
down: backup
	docker compose down

# Backup aus der laufenden DB erzeugen
backup:
	@echo "🔄 Dumping current database to $(BACKUP_FILE)..."
	docker exec $(DB_CONTAINER) sh -c 'exec mysqldump -u root -p"$${MARIADB_ROOT_PASSWORD}" "$${MARIADB_DATABASE}"' > $(BACKUP_FILE)
	@echo "✅ Backup saved."

# Backup in DB einspielen (nur wenn Datei existiert)
restore:
	@if [ -f $(BACKUP_FILE) ]; then \
		echo "📥 Restoring database from $(BACKUP_FILE)..."; \
		docker compose up -d $(DB_CONTAINER); \
		sleep 10; \
		docker exec -i $(DB_CONTAINER) sh -c 'exec mysql -u root -p"$${MARIADB_ROOT_PASSWORD}" "$${MARIADB_DATABASE}"' < $(BACKUP_FILE); \
		echo "✅ Restore complete."; \
	else \
		echo "⚠️  No backup file found, skipping restore."; \
	fi
