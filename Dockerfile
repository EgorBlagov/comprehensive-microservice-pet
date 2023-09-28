FROM python

WORKDIR /opt/service

COPY pyproject.toml poetry.lock ./

RUN pip install poetry==1.5.1
RUN poetry install --no-root
RUN poetry config virtualenvs.create false
RUN pip install fastapi uvicorn

COPY . .
