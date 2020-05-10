FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /django_server
WORKDIR /django_server
COPY /django_server/requirements.txt /django_server/
RUN pip install -r requirements.txt
COPY . /django_server/