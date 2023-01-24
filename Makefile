build:
	docker compose -f local.yml up --build -d --remove-orphans

ps:
	docker compose -f local.yml ps -a

up:
	docker compose -f local.yml up
	# docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

down_django:
	docker rm -f rbb_django

up_django:
	docker compose -f local.yml run --rm --service-ports django

show_logs:
	docker compose -f local.yml logs

migrate:
	docker compose -f local.yml run --rm django python3 manage.py migrate

makemigrations:
	docker compose -f local.yml run --rm django python3 manage.py makemigrations

collectstatic:
	docker compose -f local.yml run --rm django python3 manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm django python3 manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v

volume:
	docker volume inspect root-base-backend_rbb_postgres_data

authors-db:
	docker compose -f local.yml exec postgres psql --username=root_base_backend_user --dbname=root_base_backend

flake8:
	docker compose -f local.yml exec django flake8 .

black-check:
	docker compose -f local.yml exec django black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec django black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec django black --exclude=migrations .

isort-check:
	docker compose -f local.yml exec django isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose -f local.yml exec django isort . --diff --skip env --skip migrations

isort:
	docker compose -f local.yml exec django isort . --skip env --skip migrations
