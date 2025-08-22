PROJECT_NAME = malgucken
DB_CONTAINER = cocktail_db
DB_USER = root
DB_PASSWORD = Keins123!
BACKUP_FILE = /backup/latest.sql

.PHONY: build up down logs ps db-restore

build:
	docker compose build

up: check-db
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

ps:
	docker compose ps

# Check ob DB-Container läuft, wenn nicht: starten + Backup einspielen
check-db:
	@if [ -z "$$(docker ps -q -f name=$(DB_CONTAINER))" ]; then \
		echo "📦 Kein laufender DB-Container gefunden, starte neuen..."; \
		docker compose up -d db; \
		echo "⏳ Warte bis MariaDB bereit ist..."; \
		sleep 15; \
		if [ -f $(BACKUP_FILE) ]; then \
			echo "💾 Importiere Backup..."; \
			docker exec -i $(DB_CONTAINER) sh -c 'exec mysql -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME)' < $(BACKUP_FILE); \
		else \
			echo "⚠️ Kein Backup gefunden unter $(BACKUP_FILE)"; \
		fi \
	else \
		echo "✅ MariaDB läuft bereits, kein neuer Container nötig."; \
	fi
