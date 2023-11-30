########
# Dockerfile to build API Recipe container images
########

FROM python:3.10.12-slim

WORKDIR /usr/app/recipe

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
COPY requirements/base.txt ./requirements/base.txt
RUN pip3 install -r requirements/base.txt

COPY . .