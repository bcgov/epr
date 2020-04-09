FROM python:3.6

# Install pipenv.
RUN python -m pip install pipenv

WORKDIR /app
COPY . .

RUN pipenv install --dev

EXPOSE 8080

CMD pipenv run uvicorn main:APP --reload --host 0.0.0.0 --port 8080