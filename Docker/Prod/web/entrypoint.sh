#!/bin/sh

#python manage.py makemigrations
#python manage.py migrate

python manage.py collectstatic

gunicorn --bind 0.0.0.0:8000 tictactoe.wsgi &
#python manage.py runserver 0.0.0.0:8000

#CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "myproject.asgi:application"]
daphne -b 0.0.0.0 -p 8001 tictactoe.asgi:application
