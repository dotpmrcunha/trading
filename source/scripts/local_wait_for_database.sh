#!/bin/bash

RETRIES=5

until curl http://0.0.0.0:5432/ 2>&1 | grep '52' || [ $RETRIES -eq 0 ]
do
  echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
  sleep 1
done