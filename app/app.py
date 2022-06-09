# app.py
import uvicorn
from fastapi import FastAPI, File, UploadFile
from classification import Classification
from transcription import Transcription
from pydantic import BaseModel
import json
import logging

app = FastAPI()

logging.info("Fast Api server started")


@app.post("/generate_classification_from_audio")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    logging.info("Post received from /generate_classification_from_audio")
    file_location = f"{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    transcriber = Transcription(file_location, uploaded_file.filename)
    transcribed_text = transcriber.transcriber()

    classifier = Classification(transcribed_text)
    classifications = classifier.classifier()

    body = {
        "file_name": uploaded_file.filename,
        "classifications": classifications,
        "transcription": transcribed_text,
    }

    return {json.dumps(body)}


@app.post("/generate_transcription_from_audio")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    logging.info("Post received from /generate_transcription_from_audio")
    file_location = f"{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    transcriber = Transcription(file_location, uploaded_file.filename)
    transcribed_text = transcriber.transcriber()
    return {transcribed_text}


class Text(BaseModel):
    body: list


@app.post("/generate_classification_from_text")
async def create_upload_file(body):
    logging.info("Post received from /generate_classification_from_text")
    classifier = Classification(body)
    body = classifier.classifier()
    return {json.dumps(body)}


@app.post("/refine_transcription")
async def create_upload_file(body):
    logging.info("Post received from /refine_transcription")
    classifier = Classification(body)
    body = classifier.classifier()
    return {json.dumps(body)}


@app.get("/")
def home():
    return {"message": "Navigate to /docs to see documentation"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
