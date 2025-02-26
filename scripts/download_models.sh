mkdir -p weights
# Check if the file exists; if not, download it
[ -f "weights/RetinaFace-R50.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/RetinaFace-R50.pth' -O weights/RetinaFace-R50.pth
[ -f "weights/ParseNet-latest.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/ParseNet-latest.pth' -O weights/ParseNet-latest.pth
[ -f "weights/realesrnet_x4.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/realesrnet_x4.pth' -O weights/realesrnet_x4.pth
[ -f "weights/GPEN-BFR-512.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/GPEN-BFR-512.pth' -O weights/GPEN-BFR-512.pth
[ -f "weights/GPEN-Colorization-1024.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/GPEN-Colorization-1024.pth' -O weights/GPEN-Colorization-1024.pth

[ -f "weights/RealESRGAN_x2plus.pth" ] || wget 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth' -O weights/RealESRGAN_x2plus.pth
[ -f "weights/GFPGANv1.4.pth" ] || wget 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth' -O weights/GFPGANv1.4.pth