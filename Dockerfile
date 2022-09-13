FROM python:3.9.13
RUN apt-get -y update
RUN apt-get install -y ffmpeg
RUN python3 -m pip install --user pipx
RUN python3 -m pipx ensurepath 
SHELL ["/bin/bash", "--login", "-c"]
RUN pipx install poetry==1.2

RUN cp /root/.local/bin/poetry usr/local/bin/poetry

WORKDIR /code
COPY pyproject.toml poetry.lock /code/
RUN poetry install

COPY . /code