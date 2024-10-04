runserver:
	poetry run python manage.py runserver

install:
	poetry install

start:
	poetry run gunicorn --bind 0.0.0.0:8000 task.wsgi:application

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test
	poetry run coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	poetry run coverage xml --include=task_manager/* --omit=task_manager/settings.py