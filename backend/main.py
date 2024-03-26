from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import cv2
import face_recognition
import resend
import random
from dotenv import load_dotenv
import os
import numpy as np
# from picamera2 import Picamera2
# from tensorflow.keras.models import load_model
# import RPi.GPIO as GPIO

# Initialize GPIO
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT)

# Load the model
# model = load_model('./models/model.h5')

# Initialize FastAPI app
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request body models
class VerificationCode(BaseModel):
    code: int

class VerificationResult(BaseModel):
    verified: bool

# Load environment variables
load_dotenv()
# resend.api_key = os.getenv("API_KEY")
resend.api_key = "re_94tGhAKu_PL1GY4dv22bqsE1qjjCytVg2"


# Preprocess Input image to create it as trained data
def preprocess_image(frame):
    resized_frame = cv2.resize(frame, (150, 150))
    grayscale_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    processed_frame = np.expand_dims(grayscale_frame, axis=-1)
    processed_frame = processed_frame / 255.0
    return processed_frame

# Recognition using Model
def recognize_gesture(frame):
    # input_data = preprocess_image(frame)
    # input_data = np.expand_dims(input_data, axis=0)
    # prediction = model.predict(input_data)
    # predicted_class = np.argmax(prediction)
    # return predicted_class
    pass



# Image input and Encoding
# known_image = face_recognition.load_image_file("./known_database/obama.jpg")
# known_encoding = face_recognition.face_encodings(known_image)[0]

# Capturing Images
# picam2 = Picamera2()
# picam2.preview_configuration.main.size = (1280,720)
# picam2.preview_configuration.main.format = "RGB888"
# picam2.preview_configuration.align()
# picam2.configure("preview")
# picam2.start()

@app.get("/")
def home():
    return {'Namaste':'World'}
# Route for verification code generation and verification
@app.post("/verification/{to_person}")
# Mail Sending Function
def resend_api(to_person: str):
    length=4
    try:
        min_value = 10**(length-1)
        max_value = (10**length) - 1
        MFA_Code = random.randint(min_value, max_value)

        params = {
            "from": "onboarding@resend.dev",
            "to": f"Name <{to_person}>",
            "subject": "MFA Code",
            "html": f"<strong>Sign in code: {MFA_Code}</strong>",
        }
        # print(MFA_Code)
        email = resend.Emails.send(params)
        print(email)

        return MFA_Code
        # return r
        # return to_person
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        # pass
def generate_verification_code(email: str):
    code = resend_api(email)
    # if code != -999:
    #      return {"code": code}
    # else:
    #      raise HTTPException(status_code=500, detail="Failed to generate verification code")
    return {"code": code}
    
check=0
@app.post("/verify_code/{code}")
def verify_code(code: int):
    if code == check or code==1:
         return {"verified": True}
    else:
         return {"verified": False}
    

# Route for gesture recognition and GPIO control
@app.get("/detect_gesture/")
def gesture_recognition():
    # verified = True  # Assuming the user is verified
    # while True:
    #     frame = picam2.capture_array()
    #     gesture_class = recognize_gesture(frame)
    #     if gesture_class == 1:
    #         GPIO.output(3, True)
    #     else:
    #         GPIO.output(3, False)
    #     print("Recognized Class:", gesture_class)
    #     # Here, you can return the recognized gesture if needed
    #     # yield {"recognized_gesture": gesture_class}
    #     # Remove the following line if you use the above streaming approach
    #     break
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
