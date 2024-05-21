poetry export --without-hashes --format requirements.txt > requirements.txt

echo "Pulling base Docker image"
docker pull python:3.9-slim-bookworm

echo "Building cpu-only Docker image"
docker build \
    --platform=linux/amd64 \
    --target runtime-cpu \
    -f Dockerfile \
    -t giahuy2201/gfpgan-webui \
    .
echo "Done"