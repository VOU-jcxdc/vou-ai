from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import torch
from tts import get_tts

# Init text2speech
app = FastAPI()

class Text2Speech(BaseModel):
    text: str

@app.post("/api/speech")
def doText2Speech(body: Text2Speech):
    tts = get_tts()
    tts.tts_to_file(text=body.text, speaker_wav="resources/man.mp3", language="en", file_path="resources/output.wav")
    return FileResponse("resources/output.wav", media_type='audio/wav', filename="output.wav")