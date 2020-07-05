# Trading Backend

## Development

Pre-requisites:
 
 * Docker
 * Docker Compose
 
### Importing Initial Data

You can import initial data using:

* make import_data

This will add 4 companies in the database (AAPL, FB, GOOG and NFLX)

### Running Server locally

* make local_server

### Running Celery locally

In one terminal:
* make local_celery_worker

In another terminal:
* make local_celery_beat

## Production

To only run:
* docker-compose -f docker-compose.yml up -d

To run and import initial information:
add INITIAL=1 in config/.env.prod
