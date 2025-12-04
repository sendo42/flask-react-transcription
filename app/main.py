from fastapi import FastAPI
import uvicorn
##from uvicorn_config import config
from fastapi.responses import HTMLResponse, RedirectResponse


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/hello", response_class=HTMLResponse)
def html():
    return "hello "


@app.get("/input/audio")
def inputAudio():
    return "audio"
