# diplomatura-django-utn

![Python](https://img.shields.io/badge/observability--workflows-v1.0.0-orange)
![Python](https://img.shields.io/badge/python-v3.10.6-blue)
![Python](https://img.shields.io/badge/django-v3.2.5-lightgreen)
![Python](https://img.shields.io/badge/platform-linux--64%7Cwin--64-lightgrey)


----
<img src="doc/img/img3.png" width="800">

---

**Contenido**
- [Introduccion](#introduccion)
- [Uso](#uso)
- [Estructura aplicacion](#estructura-aplicacion)
- [Ejecutar aplicacion](#ejecutar-aplicacion)
- [Testing](#testing)
- [Crear setup](#crear-setup)
- [Documentacion](#documentacion)


## Introduccion 

Front end para la implementación de workflows de observabilidad utilizando Apache Airflow y Grafana como downstream dependencies.

## Edicion de estilos
Para poder editarlos y customizarlos luego, los colocamos en templates/
```bash
cp -r  ~/.envs/diplomatura-django-utn/lib/python3.10/site-packages/django/contrib/admin/templates/registration/ observability_workflows/templates/

cp -r  ~/.envs/diplomatura-django-utn/lib/python3.10/site-packages/django/contrib/admin/templates/admin/ observability_workflows/templates/
```

## Uso
```bash
make run
make test
make migrate
make makemigrations
make install
make sass
```

## Reconstruir staticfiles en carpeta seleccionada
```bash
python manage.py collecstatic
```

## Estructura aplicacion
<img src="doc/img/architecture.png" width="600">


## Ejecutar aplicacion
Primero hacer un build

```bash
docker-compose build
```

Luego ejecutar
```bash
docker-compose up
# daemon
docker-compose up -d
```

## Testing

## Crear setup

## Documentacion
```python
# create new project
django-admin startproject <PROJECT_NAME>
# create new app
django-admin startapp <APP_NAME>
# run development server
python manage.py runserver
# create required databases
python manage.py migrate
# create super user for admin panel
python manage.py createsuperuser
# update schemas
python manage.py makemigrations

```

## Bootstrap templates (active using)
- https://getbootstrap.com/docs/5.3/examples/
- https://getbootstrap.com/docs/5.3/examples/sidebars/
- https://getbootstrap.com/docs/5.3/examples/dashboard/

## Frontend templates
- https://github.com/codedthemes/datta-able-bootstrap-dashboard


Workaround migrations deletion: https://stackoverflow.com/questions/60521621/i-accidentally-deleted-the-migrations-folder-in-django