# Makefile für /malgucken/deploy
SHELL := /bin/bash

# Docker Compose Kommando
COMPOSE = docker-compose -f docker-compose.yml

# Backup-Datei
BACKUP_FILE = ../backup/latest.sql

# DB Service-Name aus docker-compose
DB_SERVICE = db
DB_USER ?= root
DB_PASSWORD ?= rootpassword
DB_NAME ?= BarbotDB

# Docker Netzwerk (wird automatisch aus Projektname erstellt)
DOCKER_NETWORK ?= $(shell basename $(PWD))_default

.PHONY: help up down restart logs import-db db-shell

help:
	@echo "Usage:"
	@echo "  make up        # Start all containers und importiert Backup"
	@echo "  make down      # Stop all containers"
	@echo "  make restart   # Stop + Start"
	@echo "  make logs      # Show logs for all containers"
	@echo "  make db-shell  # Open MariaDB shell"
	@echo "  make import-db # Import Backup manually"

# ----------------------------
# Container starten / stoppen
# ----------------------------
up:
	$(COMPOSE) up -d
	@$(MAKE) import-db
	@echo "Alle Container laufen und Backup wurde eingespielt."

down:
	$(COMPOSE) down

restart: down up

logs:
	$(COMPOSE) logs -f

# ----------------------------
# MariaDB Backup importieren
# ----------------------------
import-db:
	@if [ ! -f "$(BACKUP_FILE)" ]; then \
		echo "Backup Datei $(BACKUP_FILE) nicht gefunden!"; \
		exit 1; \
	fi
	@echo "Importiere Backup $(BACKUP_FILE) in die DB $(DB_NAME)..."
	docker run --rm \
		--network $(DOCKER_NETWORK) \
		-v $(realpath ../backup):/sql \
		mariadb:latest \
		sh -c "set -e; mariadb -h$(DB_SERVICE) -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME) < /sql/latest.sql"
	@echo "Backup importiert."

# ----------------------------
# MariaDB Shell
# ----------------------------
db-shell:
	docker exec -it $(DB_SERVICE) mariadb -u$(DB_USER) -p$(DB_PASSWORD) $(DB_NAME)
