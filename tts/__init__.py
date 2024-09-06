from TTS.api import TTS
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = None

def init_tts():
    try:
        global tts
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
        print("TTS model loaded successfully")
        return True
    except Exception as e:
        print(e)
        return False

def get_tts():
    global tts
    return tts

init_tts()