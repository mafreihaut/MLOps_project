# app.py
import uvicorn
from fastapi import FastAPI, File, UploadFile
from classification import Classification
import json

app = FastAPI()


@app.post("/generate_classification")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"tmp/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    classifier = Classification(file_location, uploaded_file.filename)
    body = classifier.classifier()
    return {json.dumps(body)}


@app.get("/")
def home():
    return {"message": "I'd like a taco please!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000)
