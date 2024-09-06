from fastapi import FastAPI,Response, Header
from fastapi.responses import FileResponse
from pydantic import BaseModel
from tts import TTSManager
from pathlib import Path

# Init text2speech
tts_manager = TTSManager()
app = FastAPI()
CHUNK_SIZE = 1024*1024
video_path = Path("outputs/result_voice.mp4")

class Text2Speech(BaseModel):
    text: str

@app.post("/api/speech")
def doText2Speech(body: Text2Speech):
    tts = tts_manager.get_tts()
    tts.tts_to_file(text=body.text, speaker_wav="resources/man.mp3", language="en", file_path="resources/output.wav")
    return FileResponse("resources/output.wav", media_type='audio/wav', filename="output.wav")

@app.get("/videos")
async def video_endpoint(range: str = Header(None)):
    start, end = range.replace("bytes=", "").split("-")
    start = int(start)
    end = int(end) if end else start + CHUNK_SIZE
    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start)
        filesize = str(video_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {str(start)}-{str(end)}/{filesize}',
            'Accept-Ranges': 'bytes'
        }
        return Response(data, status_code=206, headers=headers, media_type="video/mp4")