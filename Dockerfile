FROM python:3.9-slim-bookworm
WORKDIR /gfpgan-webui
# COPY pyproject.toml poetry.lock ./
COPY requirements.txt ./
RUN apt update && \
    apt install -y gcc python3-dev libc-dev libffi-dev libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 && \
    # pip install poetry && \
    pip install -r requirements.txt && \
    # poetry install --no-root --only main && \
    apt purge -y gcc python3-dev libc-dev libffi-dev && \
    rm -rf /tmp/* $HOME/.cache
COPY ./app ./app
CMD [ "python","app/main.py" ]