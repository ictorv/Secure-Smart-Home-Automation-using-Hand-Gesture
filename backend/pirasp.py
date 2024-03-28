'''
Two Level Authenication for home Automation for fully compatible with BookwormOS
'''
import cv2

import json
import gesture_detect
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
GPIO.setup(11,GPIO.OUT)










#subprocess.run(["libcamera-vid", "--codec", "libav", "-o", "test.mp4", "-t", "8000", "--width", "640", "--height", "480"])

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640,420)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

while True:

        frame= picam2.capture_array()
        cv2.imshow('Camera', frame)
        # gesture_class = recognize_gesture(frame)
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) #converting frame to image
        # gesture_class = face_recognition_handler.recognize_face(frame)
        gesture_class = gesture_detect.gesture_recognizer(image)
        prediction_dict = json.loads(gesture_class)

        # Extract the gesture class
        gesture_class = prediction_dict["Prediction"]
        if gesture_class=="palm":
            GPIO.output(11,True)
        else:
            GPIO.output(11,False)

        print("Recognized Class:", gesture_class)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()

