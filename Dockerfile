FROM arm64v8/debian:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    git \
    build-essential \
    && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

COPY . /app

CMD ["poetry", "run", "python3", "main.py"]
