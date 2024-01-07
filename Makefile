build:
	docker-compose build

run:
	docker-compose up

test:
	docker build -t web-tests .
	docker run -it web-tests pytest

lint:
	docker build -t web-tests .
	docker run -it web-tests pylint .
	docker run -it web-tests flake8 .
	docker run -it web-tests isort .
 