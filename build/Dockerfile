FROM ubuntu:jammy-20231128

LABEL maintainer="Joaquin Gonzalez <joagonzalez@gmail.com>"
LABEL application="Observability as a Service - Dashboards as a Service component"
LABEL VERSION="1.0.0"


# setup environment variable  
ENV APP_DIR=app 
ENV APP_NAME=observability_workflows
ENV APP_PORT=8000 
ENV APP_HOST=0.0.0.0

# set work directory  
RUN mkdir -p ${APP_DIR}

# where your code lives  
WORKDIR ${APP_DIR} 

# copy whole project to your docker home directory. 
COPY . ${APP_DIR} 

WORKDIR ${APP_DIR}

# Install ubuntu dependencies
RUN apt-get update
RUN apt-get install -y apt-utils vim curl make
RUN apt-get -y install python3
RUN apt-get install -y python3-dev libmysqlclient-dev
RUN ln /usr/bin/python3 /usr/bin/python 
RUN apt-get -y install python3-pip 

ENV MYSQLCLIENT_CFLAGS=-I/usr/include/mysql
ENV MYSQLCLIENT_LDFLAGS=-L/usr/lib/x86_64-linux-gnu

# install app libraries
RUN pip install -r requirements.txt 

EXPOSE 8000
CMD ["make", "run-prod"]