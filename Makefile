runserver:
	poetry run python manage.py runserver

install:
	poetry install

start:
	poetry run gunicorn --bind 0.0.0.0:8000 task.wsgi:application