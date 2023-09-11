FROM python

WORKDIR /opt/service

COPY pyproject.toml poetry.lock ./

RUN pip install poetry==1.5.1
RUN poetry config installer.max-workers 10
RUN poetry install

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
