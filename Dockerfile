FROM python:3.9.13
RUN python3 -m pip install --user pipx
RUN python3 -m pipx ensurepath 
SHELL ["/bin/bash", "--login", "-c"]
RUN pipx install poetry==1.2

WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN poetry install

COPY . /code