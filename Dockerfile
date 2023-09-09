FROM python

WORKDIR /opt/service

RUN pip install poetry
RUN poetry install
RUN uvicorn comprehensive_microservice.api_service:app

COPY . .

ENV NAME venv
