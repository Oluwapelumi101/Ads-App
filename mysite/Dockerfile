FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get -y install netcat &&  apt-get -y install gettext

# creating project directory
RUN mkdir /code
COPY . /code/
WORKDIR /code

# # create the app user
# RUN addgroup -S app && adduser -S app -G app

# Activating virtual enviroment
RUN python3 -m venv /opt/venv

# # install psycopg2 dependencies
RUN  apt-get install gcc -y
RUN apt-get install libpq-dev -y
RUN apt-get install postgresql postgresql-contrib -y

# setup
RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements4.txt && \
    chmod +x entrypoint.sh

# # # Collect static files
# RUN /opt/venv/bin/python manage.py manage.py collectstatic --noinput

# RUN chmod +x /code/entrypoint.sh
CMD ["/code/entrypoint.sh"]