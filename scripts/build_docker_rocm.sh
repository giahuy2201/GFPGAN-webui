poetry export --without-hashes --format requirements.txt > requirements.txt

echo "Pulling base rocm Docker image"
docker pull rocm/pytorch:rocm6.1_ubuntu20.04_py3.9_pytorch_2.1.2

echo "Building rocm Docker image"
docker build \
    --platform=linux/amd64 \
    --target runtime-rocm \
    -f Dockerfile \
    -t giahuy2201/gfpgan-webui:rocm \
    .
echo "Done"