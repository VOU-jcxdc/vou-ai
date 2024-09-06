from fastapi import FastAPI,Response, Header
from fastapi.responses import FileResponse
from body import Text2Speech, Text2Video
from pathlib import Path

from tts import TTSManager
from w2l import W2LManager

# Init
tts_manager = TTSManager()
w2l_manager = W2LManager(tts_manager=tts_manager)
app = FastAPI()
CHUNK_SIZE = 1024*1024

@app.post("/api/speech")
def convert_text_to_speech(body: Text2Speech):
    tts = tts_manager.get_tts()
    tts.tts_to_file(text=body.text, speaker_wav="resources/man.mp3", language="en", file_path="resources/output.wav")
    return FileResponse("resources/output.wav", media_type='audio/wav', filename="output.wav")

@app.get("/api/videos/{uuid}")
async def video_endpoint(uuid: str, range: str = Header(None)):
    video_path = Path(f'outputs/{uuid}.mp4')
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
    
@app.post("/api/videos")
async def video_endpoint(body: Text2Video):
    if not body.text:
        return Response("Bad Request", status_code=400)
    
    result = w2l_manager.convert(text=body.text, file_name_only=body.uuid)

    if (result is False):
        return {
            "statusCode": 500,
            "message": "Internal Server Error",
        }

    return {
        "statusCode": 202,
        "message": "OK",
        "data": "OK"
    }
