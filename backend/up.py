#upload/main.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles
import os
import io
import b64
import base64, binascii
from random import randint
import uuid
from PIL import Image
import face_recognition_handler
import gesture_detect

IMAGEDIR = "images/"
FACEDIR = "faces/"
PHOTODIR = "photos/"
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.post("/upload-image/")
async def create_upload_file(file: UploadFile = File(...)):
 
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
 
    #save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
 
    return {"filename": file.filename}
 
 
@app.get("/display-image/")
async def read_random_file():
 
    # get random file from the image directory
    files = os.listdir(IMAGEDIR)
    # random_index = randint(0, len(files) - 1)
 
    path = f"{IMAGEDIR}{files[0]}"
    max_label = gesture_detect.gesture_recognizer(path)

    return {"Prediction" : max_label}


@app.post("/image-verification/")
async def verify_image(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpeg"
    contents = await file.read()
 
    #save the file in photo directory
    with open(f"{PHOTODIR}{file.filename}", "wb") as f:
        f.write(contents)


    known_files = os.listdir(FACEDIR)
    unknown_files = os.listdir(PHOTODIR)
    known_path = f"{FACEDIR}{known_files[0]}"
    unknown_path = f"{PHOTODIR}{unknown_files[0]}"
    result = face_recognition_handler.recognize_face(known_path,unknown_path)
    face_recognition_handler.empty_directory(PHOTODIR)
    if result == [True]:
        return {'message':'matched!'}
    else:
        return {'message':'not matched!'}
    
@app.get("/face-verification/")
async def verify_photo(base64_str: str):

    filename = f"{uuid.uuid4()}.jpeg"
    b64.save_base64_image(base64_str,f"{PHOTODIR}{filename}")
    # return {"message":base64_str}
    # # # Get the list of known and unknown files
    known_files = os.listdir(FACEDIR)
    unknown_files = os.listdir(PHOTODIR)
    
    # Get paths for known and unknown images
    known_path = f"{FACEDIR}{known_files[0]}"
    unknown_path = f"{PHOTODIR}{unknown_files[0]}"

    # Perform face recognition
    result = face_recognition_handler.recognize_face(known_path, unknown_path)

    # Clean up the photo directory
    face_recognition_handler.empty_directory(PHOTODIR)

    # Return the result
    if result == [True]:

        return {'message': 'matched!'}
    else:
        return {'message': 'not matched!'}
@app.get("/upload-image-base/")
async def uploadb_photo(base64_str: str):

    filename = f"{uuid.uuid4()}.jpeg"
    b64.save_base64_image(base64_str,f"{FACEDIR}{filename}")

    # known_files = os.listdir(FACEDIR)

    return {"filename": filename}



