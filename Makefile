
# pipenv isn't always available, or could be pointing to the wrong place on depending on your system, 
# you may have to override it, e.g.:
# make PIPENV='python3 -m pipenv' init
PIPENV=pipenv

docker-build:
	# API
	# Run tests and linting before starting build. (build runs slowly, so this may save some time)
	cd api && make PIPENV=$(PIPENV) test
	cd api && make PIPENV=$(PIPENV) lint
	# General
	docker-compose build

docker-run:
	docker-compose up --build

docker-stop:
	docker-compose down

docker-db:
	# Run only the databse in docker.
	# Useful if you want to do local development, but don't have a postgres server.
	docker-compose run --service-ports db