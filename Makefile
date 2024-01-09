build:
	docker build -t web-tests .

run:
	docker-compose up

test:
	docker run web-tests pytest

lint:
	docker run web-tests pylint .
	docker run web-tests flake8 .
	docker run web-tests isort .
 