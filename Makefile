export PYTHONDONTWRITEBYTECODE=1
setup:
	poetry install

test:
	poetry run ./analysis/main.py 

