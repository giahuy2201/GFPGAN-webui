
from gfpgan import GFPGANer
from basicsr.utils import imwrite
import gradio as gr
import cv2
import os
import torch

from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

def inference(img):

    os.makedirs('outputs', exist_ok=True)
    # ------------------------ set up background upsampler ------------------------
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2)
    bg_upsampler = RealESRGANer(
        scale=2,
        model_path='https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth',
        model=model,
        tile=400,
        tile_pad=10,
        pre_pad=0,
        half=True)  # need to set False in CPU mode
    # bg_upsampler = None

    # ------------------------ set up GFPGAN restorer ------------------------

    # determine model paths
    model_name = 'GFPGANv1.4'
    model_path = os.path.join('models/', model_name + '.pth')

    restorer = GFPGANer(
        model_path=model_path,
        upscale=2,
        arch='clean',
        channel_multiplier=2,
        bg_upsampler=bg_upsampler)

    # ------------------------ restore ------------------------
    # read image
    img_name = os.path.basename(img)
    print(f'Processing {img_name} ...')
    basename, ext = os.path.splitext(img_name)
    input_img = cv2.imread(img, cv2.IMREAD_COLOR)

    # restore faces and background if necessary
    cropped_faces, restored_faces, restored_img = restorer.enhance(
        input_img,
        has_aligned=False,
        only_center_face=False,
        paste_back=True,
        weight=0.5)

    # save restored img
    if restored_img is not None:
        extension = ext[1:]
        save_restore_path = os.path.join('outputs', f'{basename}_fixed.{extension}')
        imwrite(restored_img, save_restore_path)
        print(f'Finished {save_restore_path} ...')
        restored_img_rgb = cv2.cvtColor(restored_img,cv2.COLOR_BGR2RGB)
        return restored_img_rgb, save_restore_path
    return -1

app = gr.Interface(
    inference, [
        gr.Image(type="filepath", label="Input"),
    ], [
        gr.Image(type="numpy", label="Output"),
        gr.File(label="Downloadable")
    ],
    title="GFPGAN",
)
print(f'ROCM: {torch.version.hip}')
app.queue()
app.launch(server_name="0.0.0.0")