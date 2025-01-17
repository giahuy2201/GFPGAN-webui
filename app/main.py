from subprocess import Popen, PIPE
import gradio as gr
import numpy as np
import cv2
import os
from pathlib import Path


def inference_gfpgan(img_path):
    return run_task("gfpgan", img_path)


def inference_gpen(img_path, task):
    return run_task("gpen", img_path, task)


def run_task(model, img_path, task="restore"):
    # do the inference in a seperate process to avoid high gpu idle power consumption of pytorch
    p = Popen(["python", "app/%s.py" % model, img_path, task], stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    print("stdout:\n", stdout)
    print("stderr:\n", stderr)
    # retrieved the restored image
    img_name = os.path.basename(img_path)
    basename, ext = os.path.splitext(img_name)
    extension = ext[1:]
    restored_img_path = os.path.join(
        "outputs", f"{basename}_{model}_{task}.{extension}"
    )
    if os.path.isfile(restored_img_path):
        restored_img = cv2.imread(restored_img_path)
        restored_img = cv2.cvtColor(restored_img, cv2.COLOR_BGR2RGB)
        print(f"Finished {model.upper()} {task} {restored_img_path}")
        return restored_img
    return -1


def get_processed_files(n=4):
    """
    Return last n files
    """
    paths = sorted(Path("outputs").iterdir(), key=os.path.getmtime)
    files = []
    for i in range(n):
        files.append(str(paths[-(i + 1)]))
    return files


with gr.Blocks(title="GFPGAN") as GFPGAN_app:
    gr.Markdown(
        """
    # GFPGAN
    """
    )
    with gr.Row():
        input_img = gr.Image(
            type="filepath", label="Input", min_width=600, sources=["upload"]
        )
        output_img = gr.Image(type="numpy", label="Output", min_width=600)
    with gr.Row():
        submit_btn = gr.Button("Submit", variant="primary", min_width=200)
        get_btn = gr.Button("Get", min_width=200)

    prev_files = gr.Gallery(
        label="Downloadables",
        show_label=False,
        elem_id="gallery",
        columns=[2],
        rows=[1],
        object_fit="contain",
        height="auto",
        allow_preview=False,
    )

    submit_btn.click(inference_gfpgan, inputs=[input_img], outputs=[output_img])
    get_btn.click(get_processed_files, outputs=[prev_files])


with gr.Blocks(title="GPEN") as GPEN_app:
    gr.Markdown(
        """
    # GPEN
    """
    )
    with gr.Row():
        input_img = gr.Image(
            type="filepath", label="Input", min_width=600, sources=["upload"]
        )
        output_img = gr.Image(type="numpy", label="Output", min_width=600)
    with gr.Row():
        task_radio = gr.Radio(["colorize", "enhance"], label="Task")
        submit_btn = gr.Button("Submit", variant="primary", min_width=200)

    submit_btn.click(
        inference_gpen, inputs=[input_img, task_radio], outputs=[output_img]
    )
    get_btn.click(get_processed_files, outputs=[prev_files])


app = gr.TabbedInterface([GFPGAN_app, GPEN_app], ["GFPGAN", "GPEN"])

app.queue()
app.launch(server_name="0.0.0.0")
