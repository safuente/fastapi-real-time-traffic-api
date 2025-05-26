## Makefile
up:
	docker-compose up --build

down:
	docker-compose down

install:
	pip install -r requirements.txt

locust:
	locust -f locustfile.py

lint:
	docker-compose run --rm app black .
