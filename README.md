# GFPGAN-webui

Based on the [original GFPGAN](https://github.com/TencentARC/GFPGAN), tailored for my use case

## Development

1. Rename the corresponding `pyproject.*.toml` file of your target runtime to `pyproject.toml`

2. Install dependencies with **Pypoetry**

```bash
poetry install --no-root
```

3. Run with `scripts/run_cpu.sh` or `scripts/run_rocm.sh` if an AMD GPU is available.

> Note that in order to run with AMD GPUs, ROCm package is required, instruction on the installation could be found over [ollama development docs](https://github.com/ollama/ollama/blob/main/docs/development.md#linux-rocm-amd).

## Build Docker images

Details could be found in `scripts/build_docker_*.sh` file

## Usage

Rename the corresponding `docker-compose.*.yaml` file of your target runtime to `docker-compose.yaml`

```bash
docker compose up -d
```
