FROM python3.10

WORKDIR /opt/service

COPY pyproject.toml poetry.lock ./

RUN pip install poetry==1.5.1
RUN poetry install --no-root

COPY . .
