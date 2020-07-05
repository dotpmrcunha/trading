FROM python:3.8
ENV LANG C.UTF-8

RUN mkdir /source
WORKDIR /source

COPY ./ .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install make automake gcc g++ subversion python3-dev postgresql postgresql-contrib

RUN pip install -r requirements.txt --no-cache-dir

ENTRYPOINT ["/source/scripts/entrypoint.sh"]