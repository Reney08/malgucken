# weil Debian scheisse ist
SHELL := /bin/bash

# Makefile für Docker-Setup im deploy-Ordner

COMPOSE = docker-compose --env-file ../.env -f docker-compose.yml
BACKUP_DIR = /malgucken/db/backup

DB_SERVICE   = mariadb
DB_USER      = $$MYSQL_USER
DB_PASSWORD  = $$MYSQL_PASSWORD
DB_NAME      = $$MYSQL_DATABASE
SQL_DUMP     ?= $(BACKUP_DIR)/latest.sql
SQL_TESTDATA ?= $(BACKUP_DIR)/testdata.sql

# Liste der Tabellen, die nach Import existieren sollen
CHECK_TABLES = Cocktail Zapfstelle Zutat Rezept users

DOCKER_NETWORK ?= $(shell basename $(PWD))_default

.PHONY: help up up-nocache up-all up-db up-web down import-db import-testdata logs status _up_main restore

help:
	@echo "Usage:"
	@echo "  make up              # Start all containers und DB importieren"
	@echo "  make up-nocache      # Build images neu, dann starten und importieren"
	@echo "  make up-all          # Alle Container starten (kein Import)"
	@echo "  make up-db           # Nur DB starten"
	@echo "  make up-web          # Nur Web starten (DB muss laufen)"
	@echo "  make down            # Alle Container stoppen"
	@echo "  make import-db       # SQL Dump importieren, falls Tabellen fehlen"
	@echo "  make import-testdata # Testdaten importieren, wenn Tabellen existieren"
	@echo "  make restore FILE=backup.sql # Backup wiederherstellen"
	@echo "  make logs            # Logs anzeigen"
	@echo "  make status          # Container Status anzeigen"

up: up-all import-db import-testdata
	@echo "Alle Services laufen und DB ist initialisiert."

up-nocache:
	@echo "Building images with --no-cache..."
	$(COMPOSE) build --no-cache
	@$(MAKE) _up_main

_up_main: up-all import-db import-testdata
	@echo "Alle Services laufen und DB ist initialisiert."

up-all:
	$(COMPOSE) up -d

up-db:
	$(COMPOSE) up -d $(DB_SERVICE)

up-web:
	$(COMPOSE) up -d web

down:
	$(COMPOSE) down

# ----------------------------
# Warten, bis DB bereit ist
# ----------------------------
wait-db:
	@echo "Waiting for database to be ready..."
	@retries=10; until $(COMPOSE) exec -T $(DB_SERVICE) \
		mariadb -u$(DB_USER) -p$(DB_PASSWORD) -e "SELECT 1;" >/dev/null 2>&1 || [ $$retries -eq 0 ]; do \
		echo "Waiting..."; \
		sleep 3; \
		retries=`expr $$retries - 1`; \
	done

# ----------------------------
# DB importieren
# ----------------------------
import-db: wait-db
	@echo "Checking if database import is needed..."
	@missing=0; \
	for table in $(CHECK_TABLES); do \
		if ! $(COMPOSE) exec -T $(DB_SERVICE) \
			mariadb -u$(DB_USER) -p$(DB_PASSWORD) -D$(DB_NAME) -e "SHOW TABLES LIKE '$$table';" | grep -q "^$$table$$"; then \
			echo "Table '$$table' is missing."; \
			missing=1; \
		fi; \
	done; \
	if [ $$missing -eq 0 ]; then \
		echo "Alle Tabellen existieren. Import wird übersprungen."; \
	else \
		echo "Eine oder mehrere Tabellen fehlen. Importiere SQL Dump..."; \
		docker run --rm \
			--network $(DOCKER_NETWORK) \
			-v $(PWD):/sql \
			mariadb:latest \
			sh -c "set -e; mariadb -h$(DB_SERVICE) -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME) < /sql/$(SQL_DUMP)"; \
		echo "Import abgeschlossen."; \
	fi

import-testdata: wait-db
	@echo "Checking if testdata import is needed..."
	@missing=0; \
	for table in $(CHECK_TABLES); do \
		if ! $(COMPOSE) exec -T $(DB_SERVICE) \
			mariadb -u$(DB_USER) -p$(DB_PASSWORD) -D$(DB_NAME) -e "SHOW TABLES LIKE '$$table';" | grep -q "^$$table$$"; then \
			echo "Table '$$table' fehlt."; \
			missing=1; \
		fi; \
	done; \
	if [ $$missing -eq 0 ]; then \
		echo "Alle Tabellen existieren. Importiere Testdaten..."; \
		docker run --rm \
			--network $(DOCKER_NETWORK) \
			-v $(PWD):/sql \
			mariadb:latest \
			sh -c "set -e; mariadb -h$(DB_SERVICE) -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME) < /sql/$(SQL_TESTDATA)"; \
		echo "Testdaten import abgeschlossen."; \
	else \
		echo "Eine oder mehrere Tabellen fehlen. Schema zuerst erstellen."; \
	fi

# ----------------------------
# Backup wiederherstellen
# ----------------------------
restore: wait-db
	@if [ -z "$(FILE)" ]; then \
		echo "Bitte Backup-Datei angeben, z. B.:"; \
		echo "  make restore FILE=$(BACKUP_DIR)/latest.sql"; \
		exit 1; \
	fi
	@echo "Restore aus $(FILE)..."
	docker run --rm \
		--network $(DOCKER_NETWORK) \
		-v $(PWD):/sql \
		mariadb:latest \
		sh -c "set -e; mariadb -h$(DB_SERVICE) -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME) < /sql/$(FILE)"
	@echo "Restore abgeschlossen."

# ----------------------------
# Logs & Status
# ----------------------------
logs:
	$(COMPOSE) logs -f

status:
	$(COMPOSE) ps

# ----------------------------
# DB Shell
# ----------------------------
db-shell:
	docker exec -it $(DB_SERVICE) mariadb -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME)
