FROM python:3.9-slim AS runtime-cpu
WORKDIR /gfpgan-webui
COPY requirements.txt ./
RUN apt update && \
    apt install -y gcc python3-dev libc-dev libgl1 libglib2.0-0 libxext6 libsm6 libxrender1 git
RUN git clone https://github.com/yangxy/GPEN.git
RUN pip install --no-cache-dir -r requirements.txt
RUN apt purge -y gcc python3-dev libc-dev libsm6 libxrender1 git && \
    apt autoremove -y && \
    rm -rf /tmp/* $HOME/.cache/*
COPY ./app ./app
CMD [ "python","-u","app/main.py" ]

FROM rocm/pytorch:rocm6.1_ubuntu20.04_py3.9_pytorch_2.1.2 AS runtime-rocm
WORKDIR /gfpgan-webui
COPY requirements.txt ./
RUN apt update && \
    apt install -y gcc python3-dev libc-dev libgl1 libglib2.0-0 libxext6 libsm6 libxrender1 git
RUN git clone https://github.com/yangxy/GPEN.git
RUN pip install --no-cache-dir -r requirements.txt
RUN apt purge -y gcc python3-dev libc-dev libsm6 libxrender1 git && \
    apt autoremove -y && \
    rm -rf /tmp/* $HOME/.cache/*
RUN apt install -y g++
COPY ./app ./app
CMD [ "python","-u","app/main.py" ]

FROM nvidia/cuda:12.8.0-base-ubuntu22.04 AS runtime-cuda
WORKDIR /gfpgan-webui
COPY requirements.txt ./
RUN apt update && \
    apt install -y gcc python3-dev python3-pip python-is-python3 libc-dev libgl1 libglib2.0-0 libxext6 libsm6 libxrender1 git
RUN git clone https://github.com/yangxy/GPEN.git
RUN pip install --no-cache-dir -r requirements.txt
RUN apt purge -y gcc python3-pip libc-dev libsm6 libxrender1 git && \
    apt autoremove -y && \
    rm -rf /tmp/* $HOME/.cache/*
COPY ./app ./app
CMD [ "python","-u","app/main.py" ]