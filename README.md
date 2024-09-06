# vou-ai
This repository provides the VOU application with virtual MC using TTS, Wav2Lip, and FastAPI.

## Getting Started
1. Install dependencies
```zsh
pip install -r requirements.txt
```
2. Start FastAPI development mode
```zsh
fastapi dev
```
3. Start FastAPI production mode
```zsh
fastapi run
```
4. Bug

If it raises 
```zsh
hp, ht, pid, tid = _winapi.CreateProcess
```
then you can fix it by install ffmpeg
```zsh
conda install ffmpeg
```
