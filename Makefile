.PHONY: build up down logs shell lint format run test

COMPOSE_FILE=devops/docker-compose.yml

build:
	docker-compose -f $(COMPOSE_FILE) build

up:
	docker-compose -f $(COMPOSE_FILE) up -d

down:
	docker-compose -f $(COMPOSE_FILE) down

logs:
	docker-compose -f $(COMPOSE_FILE) logs -f web

shell:
	docker-compose -f $(COMPOSE_FILE) exec web /bin/sh

lint:
	ruff check app
	black --check app
	isort --check-only app

format:
	ruff check app --fix
	black app
	isort app

run: down build up logs

