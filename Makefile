run:
	cd observability_workflows && python manage.py runserver 8000

migrate:
	cd observability_workflows && python manage.py migrate

makemigrations:
	cd observability_workflows && python manage.py makemigrations

test:
	python -m pytest 

install:
	pip install -r requirements.txt