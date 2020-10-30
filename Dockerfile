#FROM python:3.7-alpine
#MAINTAINER Damien Leu
#
#ENV PYTHONUNBUFFERED 1
#
#COPY ./requirements.txt /requirements.txt
#RUN pip install -r requirements.txt
#
#RUN mkdir /fitness_planner
#WORKDIR /fitness_planner
#COPY ./fitness_planner /finess_planner
#
#RUN adduser -D user
#USER user