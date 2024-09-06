import os
import subprocess

class W2LManager:
    tts_manager = None

    def __init__(self, tts_manager):
        self.tts_manager = tts_manager

    def get_tts(self):
        return self.tts_manager.get_tts()
    
    @staticmethod
    def get_project_root():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    def convert(self, text, file_name_only="output"):
        try:
            tts = self.get_tts()
            project_root = self.get_project_root()
            tts.tts_to_file(text=text, 
                            speaker_wav=f'{project_root}/resources/man.mp3', 
                            language="en", 
                            file_path=f'{project_root}/resources/{file_name_only}.wav')
            
            # Run wav2lip model
            inference_path = f'{project_root}/w2l/inference.py'
            checkpoint_path = f'{project_root}/w2l/checkpoints/wav2lip_gan.pth'
            face_path = f'{project_root}/resources/man.jpg'
            audio_path = f'{project_root}/resources/{file_name_only}.wav'
            command = [
                "python", inference_path,
                "--checkpoint_path", checkpoint_path,
                "--face", face_path,
                "--audio", audio_path,
                "--outfile", f'{project_root}/outputs/{file_name_only}.mp4'
            ]
            result = subprocess.run(command)

            return result.returncode == 0
        except Exception as e:
            print(e)
            return False