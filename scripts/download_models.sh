mkdir -p models
# Check if the file exists; if not, download it
[ -f "models/RetinaFace-R50.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/RetinaFace-R50.pth' -O models/RetinaFace-R50.pth
[ -f "models/ParseNet-latest.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/ParseNet-latest.pth' -O models/ParseNet-latest.pth
[ -f "models/realesrnet_x4.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/realesrnet_x4.pth' -O models/realesrnet_x4.pth
[ -f "models/GPEN-BFR-512.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/GPEN-BFR-512.pth' -O models/GPEN-BFR-512.pth
[ -f "models/GPEN-Colorization-1024.pth" ] || wget 'https://public-vigen-video.oss-cn-shanghai.aliyuncs.com/robin/models/GPEN-Colorization-1024.pth' -O models/GPEN-Colorization-1024.pth

[ -f "models/RealESRGAN_x2plus.pth" ] || wget 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth' -O models/RealESRGAN_x2plus.pth
[ -f "models/GFPGANv1.4.pth" ] || wget 'https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth' -O models/GFPGANv1.4.pth