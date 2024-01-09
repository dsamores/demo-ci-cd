build:
	docker build -t web-tests .

run:
	docker-compose up

test:
	docker build -t web-tests .
	docker run web-tests pytest

lint:
	docker build -t web-tests .
	docker run web-tests pylint .
	docker run web-tests flake8 .
	docker run web-tests isort .
 