#!/bin/bash

export ENV_PATH=trading/.env

docker-compose -f docker-compose.local.yml up -d

source source/scripts/local_wait_for_database.sh

source source/scripts/install.sh

python source/trading/manage.py migrate
python source/trading/manage.py runserver