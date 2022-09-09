export PYTHONDONTWRITEBYTECODE=1
setup:
	poetry install

test:
	poetry run python ./analysis/main.py 

