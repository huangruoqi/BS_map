.PHONY: test
export PYTHONDONTWRITEBYTECODE=1
setup:
	poetry install

run:
	poetry run python ./analysis/main.py 

test:
	poetry run pytest ./test

black:
	poetry run black ./analysis/
	poetry run black ./test/