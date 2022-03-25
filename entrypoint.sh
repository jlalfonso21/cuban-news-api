#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
    sleep 0.5
done

echo "PostgreSQL started"

python manage.py migrate --noinput

exec "$@"⏎                                                                      
