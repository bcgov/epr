
# pipenv isn't always available, or could be pointing to the wrong place on depending on your system, 
# you may have to override it, e.g.:
# make PIPENV='python3 -m pipenv' init
PIPENV=pipenv

run-test-lint:
	# Web
	cd web && npm run lint
	cd web && npm run test:ci
	# API
	cd api && make PIPENV=$(PIPENV) test
	cd api && make PIPENV=$(PIPENV) lint

docker-build:
	docker-compose build

docker-build-dev:
	docker-compose -f docker-compose.dev.yml build

docker-run:
	docker-compose up

docker-run-dev:
	docker-compose -f docker-compose.dev.yml up

docker-stop:
	docker-compose down

docker-db:
	# Run only the databse in docker.
	# Useful if you want to do local development, but don't have a postgres server.
	docker-compose run --service-ports db