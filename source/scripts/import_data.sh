#!/bin/bash

source source/scripts/install.sh
python source/trading/manage.py migrate

python source/trading/manage.py loaddata source/data/company.json

python source/data/fetch_initial_prices.py

python source/trading/manage.py loaddata source/data/price.json


