# Сomprehensive Microservice Pet

Here, Dmitry and I will try to build a pet project to learn some technologies widely used in Python Backend Area.
We're planning to try:

- Pydantic
- FastAPI
- SQLAlchemy + Alembic
- Poetry
- Asyncio
- Redis
- Kafka
- PostgreSQL
- Docker + Docker compose

Wow, that's a lot of stuff! Yet a lot a work to be done. We're not going to reinvent the wheel We'll just make a Pastebin clone. Some things are goingto be overcomplicated since we want to try all the techonologies listed.

Hope it's going to be fun.

God bless Dmitry's patience.

# Development

## Install

```bash
#!/bin/bash

poetry install
pre-commit install
```


## Activate venv
```bash
#!/bin/bash

poetry shell
```

## Tests
```bash
#!/bin/bash

# from venv
pytest

# without env
poetry run pytest
```
