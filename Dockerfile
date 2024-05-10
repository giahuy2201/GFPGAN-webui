FROM rocm/pytorch:rocm6.0.2_ubuntu22.04_py3.10_pytorch_2.1.2 as runtime-rocm
WORKDIR /gfpgan-webui
COPY requirements.txt ./
RUN apt update && \
    apt install -y gcc python3-dev libc-dev libffi-dev libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 && \
    pip install -r requirements.txt && \
    apt purge -y gcc python3-dev libc-dev libffi-dev && \
    rm -rf /tmp/* $HOME/.cache
COPY ./app ./app
CMD [ "python","-u","app/main.py" ]