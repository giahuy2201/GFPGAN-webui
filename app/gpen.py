from basicsr.utils.download_util import load_file_from_url
import cv2
import os,sys
from types import SimpleNamespace

# Add the custom directory to sys.path
sys.path.append('/gfpgan-webui/GPEN')
from face_enhancement import FaceEnhancement
from face_colorization import FaceColorization

# read image
task = sys.argv[2]
img_path = sys.argv[1]  # read input image from argv
img_name = os.path.basename(img_path)
print(f"Processing GPEN {img_name} ...")
basename, ext = os.path.splitext(img_name)
input_img = cv2.imread(img_path, cv2.IMREAD_COLOR)

params_dict = {
    'in_size': 512,
    'model': 'GPEN-BFR-512',
    'use_sr': True,
    'device': 'cpu',
    'channel_multiplier': 2,
    'narrow': 1,
    'sr_scale': 4,
    'key': None,
    'sr_model': 'realesrnet',
    'tile_size': 0,
    'alpha': 1,
    'aligned': 'store_true'
}

# params_dict = {
#     'in_size': 1024,
#     'model': 'GPEN-Colorization-1024',
#     'use_sr': False,
#     'device': 'cpu',
#     'channel_multiplier': 2,
#     'narrow': 1,
#     'sr_scale': 4,
#     'key': None,
#     'sr_model': 'realesrnet',
#     'tile_size': 0,
#     'alpha': 1,
#     'aligned': 'store_true'
# }
params = SimpleNamespace(**params_dict)

processor = FaceEnhancement(params, in_size=params.in_size, model=params.model, use_sr=params.use_sr, device=params.device)
# processor = FaceColorization(in_size=params.in_size, model=params.model, device=params.device)
img_out, orig_faces, enhanced_faces = processor.process(input_img, aligned=params.aligned)
restored_img = cv2.resize(img_out, img_out.shape[:2][::-1])

# save restored restored_img
if restored_img is not None:
    extension = ext[1:]
    os.makedirs("outputs", exist_ok=True)
    save_restore_path = os.path.join("outputs", f"{basename}_gpen_{task}.{extension}")
    cv2.imwrite(save_restore_path, restored_img)