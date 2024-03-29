run:
	cd observability_workflows && export DJANGO_DEBUG=1 && export DB_TYPE_SQLITE=1 && python manage.py runserver 8000

run-prod-local:
	cd observability_workflows/ && export DJANGO_DEBUG=1 && export DB_TYPE_SQLITE=0 &&  export DB_HOSTNAME=localhost && gunicorn --bind 0.0.0.0:8000 --workers=5 observability_workflows.wsgi

run-prod:
	cd observability_workflows/ && export DJANGO_DEBUG=1 && export DB_TYPE_SQLITE=0 &&  export DB_HOSTNAME=db && gunicorn --bind 0.0.0.0:8000 --workers=5 observability_workflows.wsgi

migrate:
	cd observability_workflows && python manage.py migrate

makemigrations:
	cd observability_workflows && python manage.py makemigrations

tests: 
	cd observability_workflows && python manage.py test -d --timing

test:
	# pytest -m "backend"
	cd observability_workflows && python -m pytest -W ignore::DeprecationWarning -v # -rP

install:
	pip install -r requirements.txt
	
sass:
	cd observability_workflows/static_dev && sass --update scss:css

clean:
	rm -f ./pytest_cache