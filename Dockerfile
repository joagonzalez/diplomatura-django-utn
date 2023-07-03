FROM python:3.11.4

LABEL maintainer="Joaquin Gonzalez <joagonzalez@gmail.com>"
LABEL application="Observability as a Service - Dashboards as a Service component"
LABEL VERSION="0.0.1"

COPY ./ /src/

WORKDIR /src/

RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  

WORKDIR /src/observability_workflows

EXPOSE 8000  

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]