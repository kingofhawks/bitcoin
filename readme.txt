How to run django celery tasks:
cd to bitcoin directory
manage.py celery worker
manage.py celery beat -lDEBUG -S djcelery.schedulers.DatabaseScheduler