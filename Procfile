web: python manage.py migrate && python manage.py collectstatic && gunicorn mysite.wsgi
release: python manage.py makemigrations && python manage.py migrate