#!/bin/bash

if [ "$DATABASES_DEFAULT_NAME" = "trading_database" ]
then
    echo "Waiting for trading_database..."

    RETRIES=5

    until curl http://$DATABASES_DEFAULT_HOST:$DATABASES_DEFAULT_PORT/ 2>&1 | grep '52' || [ $RETRIES -eq 0 ]
    do
      echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
      sleep 2
    done

    echo "PostgreSQL started"
fi

python manage.py migrate

if [ $INITIAL = 1 ]
then
    echo "Importing Initial data..."
    python manage.py loaddata ../data/company.json
    export DATA_BASE=../data
    python ../data/fetch_initial_prices.py
    python manage.py loaddata ../data/price.json
fi

exec "$@"