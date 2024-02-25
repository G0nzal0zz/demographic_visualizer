#!/bin/bash

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "MySQL started"
fi

# Uncomment to delete the db on each restart (danger)
# echo "Clear entire database"
# python manage.py flush --no-input

# Uncomment to apply migrations on each restart
# echo "Appling database migrations..."
# python3 manage.py runserver

exec "$@"