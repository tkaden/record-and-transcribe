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

def custom_flagging_function(flag_data):
    # Create a directory for flagged data if it doesn't exist
    os.makedirs("flagged_data", exist_ok=True)

    # Generate a unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"flagged_data/flagged_{timestamp}.txt"

    # Write the transcribed text to a file
    with open(filename, "w") as file:
        file.write(flag_data["output"])

demo = gr.Interface(
    transcribe,
    gr.Audio(sources=["microphone"], type="numpy", label="Record Audio"),
    "text",
    flagging_callback=custom_flagging_function
)

demo.launch()
