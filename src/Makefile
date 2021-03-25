clean-db:
	@find accounts/migrations -type f -not -name __init__.py -delete && \
	find website/migrations -type f -not -name __init__.py -delete && \
	rm -rf db.sqlite3

update-db:
	@python manage.py makemigrations && python manage.py migrate