echo "Building cpu-only Docker image"
docker build \
    --platform=linux/${TARGETARCH} \
    -f Dockerfile \
    -t giahuy2201:${TARGETARCH} \
    .
echo "Done"

echo "Building rocm Docker image"
docker build \
    --platform=linux/${TARGETARCH} \
    --target runtime-rocm \
    -f Dockerfile \
    -t giahuy2201:${TARGETARCH} \
    .
echo "Done"