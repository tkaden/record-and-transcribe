import gradio as gr
from transformers import pipeline
import numpy as np
import os
from datetime import datetime

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

def transcribe(audio):
    if audio is None:
        return "No audio received"

    try:
        sr, y = audio
        y = y.astype(np.float32)
        y /= np.max(np.abs(y))

        return transcriber({"sampling_rate": sr, "raw": y})["text"]
    except Exception as e:
        return f"Error processing audio: {e}"

demo = gr.Interface(
    transcribe,
    gr.Audio(sources=["microphone"], type="numpy", label="Record Audio"),
    "text",
)

demo.launch()
