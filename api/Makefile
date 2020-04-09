
# pipenv isn't always available, or could be pointing to the wrong place on depending on your system, 
# you may have to override it, e.g.:
# make PIPENV='python3 -m pipenv' init
PIPENV=pipenv

init:
	# Create virtual environment using pipenv.
	$(PIPENV) install --dev

test:
	# Run tests in virtual environment.
	$(PIPENV) run python -m unittest

lint:
	# Run lint in virtual environment.
	$(PIPENV) run pylint --rcfile=.pylintrc *.py **/*.py

run:
	# Run the application in the virtual environment (after linting and testing).
	$(PIPENV) run pylint --rcfile=.pylintrc *.py **/*.py
	$(PIPENV) run python -m unittest
	$(PIPENV) run uvicorn main:APP --reload --port 8080

notebook:
	# Run jupyter notebooks.
	$(PIPENV) run jupyter notebook

shell:
	# Run shell in virtual environment shell.
	$(PIPENV) shell

docker-dev-test:
	# Run tests in docker.
	docker-compose -f ../docker-compose.dev.yml run api-dev scripts/test.sh

docker-dev-lint:
	# Run lint in docker.
	docker-compose -f ../docker-compose.dev.yml run api-dev scripts/lint.sh
