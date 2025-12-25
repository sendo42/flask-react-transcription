from fastapi import FastAPI, File, UploadFile
import uvicorn
##from uvicorn_config import config
from fastapi.responses import HTMLResponse, RedirectResponse
import whisper
import time
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World" : "Hello World"}

@app.get("/hello", response_class=HTMLResponse)
def html():
    return "hello "



@app.post("/uploadAudio")
async def uploadAudio(file: UploadFile = File(...)):
    print("成功")
    return {"filename" : file.filename}

@app.get("/transcribe-blocking")
async def transcribe_audio_blocking():
    model = whisper.load_model("turbo")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio("./test/test.m4a")
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)


