bootstrap:
	poetry update

build:
	poetry run mkdocs build

serve:
	poetry run mkdocs serve

deploy:
	poetry run mkdocs gh-deploy --force