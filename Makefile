runserver:
	poetry run python manage.py runserver

start:
	poetry run gunicorn --bind 0.0.0.0:8000 task.wsgi