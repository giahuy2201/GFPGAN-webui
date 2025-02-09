from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer
from gfpgan import GFPGANer
import cv2
import os
import sys
from _utils import resize_image

WEIGHTS_PATH = "/gfpgan-webui/weights"
RealESRGAN_URL = "%s/RealESRGAN_x2plus.pth" % WEIGHTS_PATH
GFPGAN_URL = "%s/GFPGANv1.4.pth" % WEIGHTS_PATH

# ------------------------ set up background upsampler ------------------------

withGPU = True if "WITH_GPU" in os.environ else False

model = RRDBNet(
    num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2
)
bg_upsampler = RealESRGANer(
    scale=2,
    model_path=RealESRGAN_URL,
    model=model,
    tile=400,
    tile_pad=10,
    pre_pad=0,
    half=withGPU,
)  # need to set False in CPU mode
# bg_upsampler = None

# ------------------------ set up GFPGAN restorer ------------------------

restorer = GFPGANer(
    model_path=GFPGAN_URL,
    upscale=2,
    arch="clean",
    channel_multiplier=2,
    bg_upsampler=bg_upsampler,
)

# ------------------------ restore ------------------------

# read image
resize = sys.argv[3]
task = sys.argv[2]
img_path = sys.argv[1]  # read input image from argv
img_name = os.path.basename(img_path)
basename, ext = os.path.splitext(img_name)
input_img = cv2.imread(img_path, cv2.IMREAD_COLOR)
# downsize input image
if resize == "on":
    input_img = resize_image(input_img)

# restore faces and background if necessary
cropped_faces, restored_faces, restored_img = restorer.enhance(
    input_img, has_aligned=False, only_center_face=False, paste_back=True, weight=0.5
)

# save restored img
if restored_img is not None:
    extension = ext[1:]
    os.makedirs("outputs", exist_ok=True)
    save_restore_path = os.path.join("outputs", f"{basename}_gfpgan_{task}.{extension}")
    cv2.imwrite(save_restore_path, restored_img)
