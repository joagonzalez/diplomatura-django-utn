FROM ubuntu:jammy-20231128

LABEL maintainer="Joaquin Gonzalez <joagonzalez@gmail.com>"
LABEL application="Observability as a Service - Dashboards as a Service component"
LABEL VERSION="1.0.0"


# setup environment variable  
ENV APP=observability_workflows
ENV APP_NAME=/var/www/html/${APP}
ENV APACHE_DIR=/var/www/html 
ENV APP_PORT=8000 
ENV APP_HOST=0.0.0.0

# set work directory  
RUN mkdir -p ${APP_NAME}

# where your code lives  
WORKDIR ${APP_NAME} 

# copy whole project to your docker home directory. 
COPY . ${APP_NAME} 
RUN ls ${APP_NAME}

# Install ubuntu dependencies
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils 
RUN apt-get -y install python3 libapache2-mod-wsgi-py3 
RUN ln /usr/bin/python3 /usr/bin/python 
RUN apt-get -y install python3-pip 

# Install python libraries
RUN pip install django ptvsd 
ADD ./site-config.conf /etc/apache2/sites-available/000-default.conf 
ADD ./requirements.txt ${APACHE_DIR}

WORKDIR ${APACHE_DIR}
RUN pip install -r requirements.txt 

# Enable permissions for folders and database files
RUN chmod 664 ${APP_NAME}/${APP}/db.sqlite3 
RUN chmod 775 ${APP_NAME}/${APP}
RUN chmod -R 775 ${APP_NAME}/${APP}/static_dev
RUN chmod 775 ${APP_NAME}/${APP}/media
RUN chmod 775 ${APP_NAME}/${APP}/static_dev/robots.txt
RUN chmod 775 ${APP_NAME}/${APP}/static_dev/favicon.ico
RUN chown :www-data ${APP_NAME}/${APP}/db.sqlite3 
RUN chown :www-data ${APP_NAME}/${APP}
RUN chown :www-data ${APP_NAME}/${APP}/static_dev
RUN chown :www-data ${APP_NAME}/${APP}/media
RUN chown :www-data ${APP_NAME}/${APP}/static_dev/robots.txt
RUN chown :www-data ${APP_NAME}/${APP}/static_dev/favicon.ico
# In case not using default apache logs files/folders
# RUN chmod 775 ${APP_NAME}/${APP}/logs 
# RUN chown :www-data ${APP_NAME}/${APP}/logs 


EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]