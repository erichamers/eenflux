clean-db:
	@find src/accounts/migrations -type f -not -name __init__.py -delete && \
	find src/website/migrations -type f -not -name __init__.py -delete && \
	rm -rf src/db.sqlite3

update-db:
	@python ./src/manage.py makemigrations && python ./src/manage.py migrate

run:
	@python ./src/manage.py runserver