# these will speed up builds, for docker-compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all: down build up firstdbsetup

build:
	docker-compose build

up:
	docker-compose up -d django-project

down:
	docker-compose down

harddown: down
	sudo rm -r .data/db

firstdbsetup:
	docker-compose run --rm django-project python3 manage.py migrate
	docker-compose run --rm django-project python3 manage.py shell --command="from django.contrib.auth.models import Group; Group.objects.create(name='admin'); Group.objects.create(name='employee')"
	docker-compose run --rm django-project python3 manage.py createsuperuser

logs:
	docker-compose logs django-project | tail -100

test:
	pytest --tb=short

flake8:
	flake8
