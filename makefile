bash:
	docker run --rm \
	-v $(PWD):/app \
	-w /app \
	-it python:3.10 \
	bash

update_version:
	docker run --rm \
	-v $(PWD):/app \
	-w /app \
	-it python:3.10 \
	python version.py

update_dockerfile:
	docker run --rm \
	-v $(PWD):/app \
	-w /app \
	-it python:3.10 \
	python apply-templates.py

generate_dockerhub_push:
	docker run --rm \
	-v $(PWD):/app \
	-w /app \
	-it python:3.10 \
	python auto-push.py