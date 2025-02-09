poetry export --without-hashes --format requirements.txt > requirements.txt

echo "Building cuda Docker image"
docker build \
    --platform=linux/amd64 \
    --target runtime-cuda \
    -f Dockerfile \
    -t giahuy2201/gfpgan-webui:cuda \
    .
echo "Done"