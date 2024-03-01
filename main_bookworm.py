'''
Two Level Authenication for home Automation for fully compatible with BookwormOS
'''
import cv2
import face_recognition
import resend
import random
from dotenv import load_dotenv
import os
import numpy as np
from picamera2 import Picamera2
from tensorflow.keras.models import load_model
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
model = load_model('./models/model.h5')

'''Preprocess Input image to create it as trained data'''
def preprocess_image(frame):
    resized_frame = cv2.resize(frame, (150, 150))
    grayscale_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    processed_frame = np.expand_dims(grayscale_frame, axis=-1)
    processed_frame = processed_frame / 255.0
    return processed_frame

'''Recognition using Model'''
def recognize_gesture(frame):
    input_data = preprocess_image(frame)
    input_data = np.expand_dims(input_data, axis=0)
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction)
    return predicted_class

'''Security Key'''
load_dotenv()
resend.api_key = "API_KEY_HERE" # Add API KEY 

'''Mail Sending Function'''
def resend_api(to_person: str, length=4):
    try:
        min_value = 10**(length-1)
        max_value = (10**length) - 1
        MFA_Code = random.randint(min_value, max_value)

        params = {
            "from": "onboarding@resend.dev",
            "to": ["victor.myid@gmail.com"],
            "subject": "MFA Code",
            "html": f"<strong>Sign in code: {MFA_Code}</strong>"
        }
        print(MFA_Code)
        r = resend.Emails.send(params)
        print(r)

        return MFA_Code
    except:
        return -999

'''Image input and Encoding'''
known_image = face_recognition.load_image_file("./known_database/obama.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

'''Flag variable'''
loop=1
verified=0

'''Capturing Images'''
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280,720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

'''Recognition and Mail'''
while True:
    #ret, frame = cap.read()
    frame= picam2.capture_array()
    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Compare each face encoding with the known face encoding
    for face_encoding in face_encodings:
        # Compare the current face encoding with the known face encoding
        match = face_recognition.compare_faces([known_encoding], face_encoding)

        # If a match is found, label the face
        if match[0]:
            loop=0 # For ending loop
            verified=1 # To send flag that verified person want to access
            cv2.destroyAllWindows()
            if __name__ == "__main__":
                code=resend_api("victor.myid@gmail.com")
                check=int(input("Enter Verification Code:"))
                if (code == check) and (code!=-999):
                    print("Verification Completed!")
       
    if loop:
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        cv2.destroyAllWindows()
        break

'''Recogniton and GPIO Control'''
if verified:
    while True:
        frame= picam2.capture_array()
        cv2.imshow('Camera', frame)
        gesture_class = recognize_gesture(frame)
        if gesture_class==1:
            GPIO.output(3,True)
        else:
            GPIO.output(3,False)
            #GPIO.output(11,False)
        #if gesture_class==3:
            #GPIO.output(11,False)
        print("Recognized Class:", gesture_class)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()