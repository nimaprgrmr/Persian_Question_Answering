from fastapi import FastAPI, File, UploadFile
import os
from secrets import token_hex
from SpeechRecognition import converter, converter_with_corrector


app = FastAPI(title="Convert Speech Too Text")


@app.get("/print-name")
def print_name(name: str):
    return "hello "+name


@app.post("/upload")
async def audio_tp_text(file: UploadFile = File(...)):
    file_ext = file.filename.split(".").pop()
    file_name = token_hex(10)
    file_path = f"{file_name}.{file_ext}"
    with open(file_path, 'wb') as f:
        content = await file.read()
        f.write(content)
    text_output, time_output = converter_with_corrector(file_path)
    os.remove(file_path)
    return {"success": True, "message": "File Uploaded successfully", "speech2text": text_output, "time": time_output}
