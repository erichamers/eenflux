clean-db:
	@find src/accounts/migrations -type f -not -name __init__.py -delete && \
	find src/website/migrations -type f -not -name __init__.py -delete && \
	rm -rf src/db.sqlite3

update-db:
	@venv/bin/python3.9 ./src/manage.py makemigrations && venv/bin/python3.9 ./src/manage.py migrate

run:
	@venv/bin/python3.9 ./src/manage.py runserver