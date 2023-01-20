#!/bin/bash
set -e


echo "Creating migrations..."
python manage.py makemigrations
echo "Created!"

echo "Migrating models..."
python manage.py migrate --noinput
echo "Migrated!"

echo "Loading all fixtures..."
# python manage.py loaddata **/fixtures/*.json
echo "Loaded!"

if [ "$MODE" = "production" ]; then
    echo "Coping default media..."
    mkdir -p /var/www/pegabus/media/
    cp -a pegabus/media/. /var/www/pegabus/media/
    echo "Done"

    echo "Collecting statics..."
    python manage.py collectstatic --noinput -v 0
    echo "Collected"

    echo "Starting clinica as `whoami`"
    exec gunicorn pegabus.wsgi:application --name pegabus \
        --timeout 300 \
        --workers $NUM_GUNICORN_WORKERS --bind 0.0.0.0:$DJANGO_PORT --log-level=info \
        --log-file=$LOGS_ROOT/gunicorn_log.log --access-logfile=$LOGS_ROOT/gunicorn_access.log

elif [ "$MODE" = "development" ]; then
    echo "Starting pegabus 3.0..."
    python manage.py runserver 0.0.0.0:8080
fi
