run:
	cd observability_workflows && export DJANGO_DEBUG=1 && python manage.py runserver 8000

run-prod:
	cd observability_workflows && export DJANGO_DEBUG=0 && python manage.py runserver 8000

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