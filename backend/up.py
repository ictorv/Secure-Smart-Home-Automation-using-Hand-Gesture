#upload/main.py
from fastapi import FastAPI, File, UploadFile,HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import email_send
import os
import sqlite3
import b64
import sqldb
import uuid

import face_recognition_handler
import gesture_detect

IMAGEDIR = "images/"
FACEDIR = "faces/"
PHOTODIR = "photos/"


class UserDetails(BaseModel):
    email: str
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

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





@app.post("/insert/")
async def insert_details(user_details: UserDetails):
    try:
        # Connect to SQLite database
        sqldb.insertDetails(user_details.email,user_details.username,user_details.password)

        return {"message": "Details inserted into the table"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    



@app.get("/user/{username}")
async def retrieve_user_details(username: str):
    try:
        # Connect to the SQLite database
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()

        # Retrieve user details from the database
        cursor.execute("SELECT * FROM User WHERE User_Name=?", (username,))
        user_details = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        sqliteConnection.close()

        # Check if user exists
        if user_details:
            email, user_name, password = user_details
            return {
                "Email": email,
                "Username": user_name,
                "Password": password
            }
        else:
            raise HTTPException(status_code=404, detail="User not found")

    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve user details: {str(error)}")
    


@app.post("/login/")
async def login(login_request: LoginRequest):
    try:
        # Connect to the SQLite database
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()

        # Retrieve user details from the database
        cursor.execute("SELECT * FROM User WHERE User_Name=?", (login_request.username,))
        user_details = cursor.fetchone()

        # Close the cursor and connection
        cursor.close()
        sqliteConnection.close()

        # Check if user exists and password matches
        if user_details:
            email, user_name, stored_password = user_details
            if login_request.password == stored_password:
                otp=email_send.send_email()
                

                return {"message": otp}
            else:
                raise HTTPException(status_code=401, detail="Incorrect password")
        else:
            raise HTTPException(status_code=404, detail="User not found")

    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail=f"Failed to perform login: {str(error)}")
    

@app.post("/verify-otp/")
async def verify_otp(username: str, otp: str):
    try:
        # Connect to the SQLite database
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()

        # Retrieve user details from the database
        cursor.execute("SELECT OTP FROM User WHERE User_Name=?", (username,))
        stored_otp = cursor.fetchone()

        # Check if OTP matches
        if stored_otp and otp == stored_otp[0]:
            return {"message": otp}
        else:
            raise HTTPException(status_code=401, detail="Incorrect OTP")

    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail=f"Failed to verify OTP: {str(error)}")
    finally:
        cursor.close()
        sqliteConnection.close()