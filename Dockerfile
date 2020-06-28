FROM python:3.7

ENV PROJECT fancycam

RUN apt-get update && apt-get install -y curl make rsync vim

COPY docker-config/bashrc /root/.bashrc

WORKDIR /opt/${PROJECT}

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN ln -s /root/.poetry/bin/poetry /usr/local/bin/

COPY ${PROJECT}/poetry.lock /opt/${PROJECT}/poetry.lock
COPY ${PROJECT}/pyproject.toml /opt/${PROJECT}/pyproject.toml
COPY ${PROJECT} /opt/${PROJECT}

RUN poetry config virtualenvs.create false
RUN poetry install
