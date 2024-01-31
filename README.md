# GFPGAN-webui

Based on the [original GFPGAN](https://github.com/TencentARC/GFPGAN), tailored for my use case

## Development
```bash
poetry install --no-root
poetry run python app/main.py
# OR for amdgpu
./start-rocm.sh
```

## Build
```bash
poetry export --without-hashes --format requirements.txt > requirements.txt
docker build -t giahuy2201/gfpgan-webui .
```

## Usage
```bash
docker compose up -d
```