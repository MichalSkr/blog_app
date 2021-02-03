python manage.py collectstatic --no-input
python manage.py makemigrations blog_app
python manage.py migrate blog_app
python manage.py migrate
uwsgi uwsgi.ini 