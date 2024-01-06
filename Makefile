# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all: down build up test

build:
	docker-compose build

up:
	docker-compose up -d django-project

down:
	docker-compose down

harddown: down
	sudo rm -r .data/db

logs:
	docker-compose logs django-project | tail -100

test:
	pytest --tb=short

flake8:
	flake8
