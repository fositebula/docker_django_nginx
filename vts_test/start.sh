#!/bin/bash
#命令只执行最后一个,所以用 &&
#python manage.py collectstatic --noinput
#python manage.py makemigrations
#python manage.py migrate --fake pay zero
#python manage.py showmigrations
#python manage.py migrate --fake pay zero
#python manage.py makemigrations
#python manage.py migrate --fake-initial
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
supervisord
gunicorn vts_test.wsgi:application -c gunicorn.conf
