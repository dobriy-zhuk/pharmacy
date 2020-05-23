FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /pharmacy_site
WORKDIR /pharmacy_site
COPY /pharmacy_site/requirements.txt /django_server/
RUN pip install -r requirements.txt
COPY . /pharmacy_site/