FROM python:3.10-slim

COPY . /usr/local/report_api

WORKDIR /usr/local/report_api

RUN apt-get update

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install

EXPOSE ${API_PORT_IN}

CMD ["poetry", "run", "server"]
