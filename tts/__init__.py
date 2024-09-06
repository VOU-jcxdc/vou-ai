from TTS.api import TTS
import torch

class TTSManager:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = None

        try:
            self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
            print("TTS model loaded successfully")
        except Exception as e:
            print(e)

    def get_tts(self):
        return self.tts