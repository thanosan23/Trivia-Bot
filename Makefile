all: build run

build:
	docker-compose build

run:
	docker-compose up -d
	python3 main.py

