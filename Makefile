
install:
	sh source/scripts/install.sh

import_data:
	sh source/scripts/import_data.sh

local_server:
	sh source/scripts/local_server.sh

local_celery_worker:
	sh source/scripts/local_celery_worker.sh

local_celery_beat:
	sh source/scripts/local_celery_beat.sh