'''
Two Level Authenication for home Automation for fully compatible with BookwormOS
'''
import cv2

import json
import gesture_detect
import numpy as np
from picamera2 import Picamera2
import requests

import RPi.GPIO as GPIO

gesture_classes = [
    'palm',
    'ok',
    'peace_inverted',
    'two_up_inverted',
    'rock'
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

SERVER_BASE_URL = 'http://127.0.0.1:8001'

def capture_and_average_frames():
    frames = []
    for _ in range(7):
        frame = picam2.capture_array()
        frames.append(frame)
    averaged_frame = np.mean(frames, axis=0).astype(np.uint8)
    return averaged_frame

def send_image_to_server(image):
    url = f'{SERVER_BASE_URL}/predict/inference_server'
    files = {'file': ('image.jpg', image, 'multipart/form-data')}
    response = requests.post(url, files=files)
    return response.json()

try:
    while True:
        averaged_frame = capture_and_average_frames()
        cv2.imshow('Camera', averaged_frame)

        # Convert the frame to JPEG format
        _, image = cv2.imencode('.jpg', averaged_frame)
        response = send_image_to_server(image)

        # Extract the gesture class and score from the response
        gesture_class = response.get('label')
        score = response.get('score')

        # Process the gesture class
        if gesture_class == "palm":
            GPIO.output(11, True)
        else:
            GPIO.output(11, False)

        print("Recognized Class:", gesture_class)
        print("Score:", score)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    picam2.stop()
    GPIO.cleanup()
    cv2.destroyAllWindows()