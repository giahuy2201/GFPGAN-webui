import cv2
import os, sys
import torch
from types import SimpleNamespace
from _utils import resize_image

# Add the custom directory to sys.path
sys.path.append("/gfpgan-webui/GPEN")
from face_enhancement import FaceEnhancement
from face_colorization import FaceColorization

# check for gpu
withGPU = True if torch.cuda.is_available() else False

# read image
resize = sys.argv[3]
task = sys.argv[2]
img_path = sys.argv[1]  # read input image from argv
img_name = os.path.basename(img_path)
basename, ext = os.path.splitext(img_name)
img_in = cv2.imread(img_path, cv2.IMREAD_COLOR)


def colorize(img_in):
    params_dict = {
        "in_size": 1024,
        "model": "GPEN-Colorization-1024",
        "use_sr": False,
        "device": "cuda" if withGPU else "cpu",
        "channel_multiplier": 2,
        "narrow": 1,
        "sr_scale": 4,
        "key": None,
        "sr_model": "realesrnet",
        "tile_size": 0,
        "alpha": 1,
        "aligned": True,
    }
    params = SimpleNamespace(**params_dict)
    processor = FaceColorization(
        in_size=params.in_size, model=params.model, device=params.device
    )
    img_out, orig_faces, enhanced_faces = processor.process(
        img_in, aligned=params.aligned
    )
    return cv2.resize(img_out, img_out.shape[:2][::-1])


def restore(img_in):
    params_dict = {
        "in_size": 512,
        "model": "GPEN-BFR-512",
        "use_sr": True,
        "device": "cuda" if withGPU else "cpu",
        "channel_multiplier": 2,
        "narrow": 1,
        "sr_scale": 4,
        "key": None,
        "sr_model": "realesrnet",
        "tile_size": 0,
        "alpha": 1,
        "aligned": True,
    }
    params = SimpleNamespace(**params_dict)
    processor = FaceEnhancement(
        params,
        in_size=params.in_size,
        model=params.model,
        use_sr=params.use_sr,
        device=params.device,
    )
    # downsize input image
    if resize == "on":
        img_in = resize_image(img_in)
    img_out, orig_faces, enhanced_faces = processor.process(
        img_in, aligned=params.aligned
    )
    # return enhanced_faces[0][:,:,::-1]
    return cv2.resize(img_out, img_out.shape[:2][::-1])


img_result = None

if task == "restore":
    img_result = restore(img_in)
elif task == "colorize":
    img_result = colorize(img_in)
else:
    print("Unsupported task: %s" % task)

# save result
if img_result is not None:
    extension = ext[1:]
    os.makedirs("outputs", exist_ok=True)
    save_restore_path = os.path.join("outputs", f"{basename}_gpen_{task}.{extension}")
    cv2.imwrite(save_restore_path, img_result)
