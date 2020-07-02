FROM python:3.8.3-alpine3.12
ENV LANG C.UTF-8

RUN mkdir /source
WORKDIR /source
RUN mkdir /source/static

COPY ./ .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

pip install -r requirements.txt --no-cache-dir

ENTRYPOINT ["/source/scripts/entrypoint.sh"]