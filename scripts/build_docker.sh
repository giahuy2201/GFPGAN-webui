poetry export --without-hashes --format requirements.txt > requirements.txt

echo "Building cpu-only Docker image"
docker build \
    --platform=linux/amd64 \
    --target runtime-cpu \
    -f Dockerfile \
    -t giahuy2201/gfpgan-webui \
    .
echo "Done"

echo "Building rocm Docker image"
docker build \
    --platform=linux/amd64 \
    --target runtime-rocm \
    -f Dockerfile \
    -t giahuy2201/gfpgan-webui:rocm \
    .
echo "Done"