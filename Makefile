runserver:
	poetry run python manage.py runserver

install:
	poetry install

start:
	poetry run gunicorn task.wsgi:application