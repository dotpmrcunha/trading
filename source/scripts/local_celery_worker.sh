#!/bin/bash

docker-compose -f docker-compose.local.yml up -d

source source/scripts/local_wait_for_database.sh

source source/scripts/install.sh

python source/trading/manage.py migrate
cd source/trading
celery -A trading worker -l info