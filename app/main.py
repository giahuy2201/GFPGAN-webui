from subprocess import Popen, PIPE
import gradio as gr
import numpy as np
import cv2
import os
from pathlib import Path


def inference(img_path):
    # do the inference in a seperate process to avoid high gpu idle power consumption of pytorch
    p = Popen(["python", "app/inference.py", img_path], stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    print("stdout:\n", stdout)
    print("stderr:\n", stderr)
    print(f"inference process {p.pid} finished")
    # retrieved the restored image
    img_name = os.path.basename(img_path)
    basename, ext = os.path.splitext(img_name)
    extension = ext[1:]
    restored_img_path = os.path.join("outputs", f"{basename}_fixed.{extension}")
    if os.path.isfile(restored_img_path):
        restored_img = cv2.imread(restored_img_path)
        restored_img = cv2.cvtColor(restored_img, cv2.COLOR_BGR2RGB)
        print(f"Finished {restored_img_path}")
        return restored_img, restored_img_path
    return -1


with gr.Blocks(title="GFPGAN") as app:
    gr.Markdown(
        """
    # GFPGAN
    """
    )
    with gr.Row():
        input_img = gr.Image(type="filepath", label="Input", min_width=600)
        output_img = gr.Image(type="numpy", label="Output", min_width=600)
    submit_btn = gr.Button("Submit")
    submit_btn.click(inference, inputs=[input_img], outputs=[output_img])

app.queue()
app.launch(server_name="0.0.0.0")
