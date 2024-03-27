'''
Two Level Authenication for home Automation for fully compatible with BookwormOS
'''
import cv2
import face_recognition
import face_recognition_handler
# import resend
import json
# import random
# from dotenv import load_dotenv
# import os
import numpy as np
from picamera2 import Picamera2

import RPi.GPIO as GPIO

gesture_classes = [
    "call",
    "dislike",
    "fist",
    "four",
    "like",
    "mute",
    "ok",
    "one",
    "palm",
    "peace",
    "peace_inverted",
    "rock",
    "stop",
    "stop_inverted",
    "three",
    "three2",
    "two_up",
    "two_up_inverted"
]


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)



# '''Flag variable'''
# loop=1
# verified=0

'''Capturing Images'''
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1280,720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# '''Recognition and Mail'''
# while True:
#     #ret, frame = cap.read()
#     frame= picam2.capture_array()
#     # Find all face locations in the frame
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     # Compare each face encoding with the known face encoding
#     for face_encoding in face_encodings:
#         # Compare the current face encoding with the known face encoding
#         match = face_recognition.compare_faces([known_encoding], face_encoding)

#         # If a match is found, label the face
#         if match[0]:
#             loop=0 # For ending loop
#             verified=1 # To send flag that verified person want to access
#             cv2.destroyAllWindows()
#             if __name__ == "__main__":
#                 code=resend_api("victor.myid@gmail.com")
#                 check=int(input("Enter Verification Code:"))
#                 if (code == check) and (code!=-999):
#                     print("Verification Completed!")
       
#     if loop:
#         cv2.imshow('Video', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         cv2.destroyAllWindows()
#         break

'''Recogniton and GPIO Control'''
# if verified:
while True:
    frame= picam2.capture_array()
    cv2.imshow('Camera', frame)
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) #converting frame to image
        # gesture_class = face_recognition_handler.recognize_face(frame)
    gesture_class = face_recognition_handler.recognize_face(image)
    prediction_dict = json.loads(gesture_class)

    # Extract the gesture class
    gesture_class = prediction_dict["Prediction"]
    if gesture_class=="palm":
        GPIO.output(3,True)
    else:
        GPIO.output(3,False)

    print("Recognized Class:", gesture_class)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()