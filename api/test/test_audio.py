from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_wav():
    wav_bytes = b"FAKE-WAV-DATA"  
    files = {
        "file": ("test.wav", wav_bytes, "audio/wav")
    }
    response = client.post("/uploadAudio", files=files)

    assert response.status_code == 200
    assert response.json()["filename"] == "test.wav"

