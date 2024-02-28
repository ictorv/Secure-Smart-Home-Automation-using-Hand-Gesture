import cv2
import numpy as np
import subprocess
from tensorflow.keras.models import load_model
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)

model = load_model('model.h5')
subprocess.run(["libcamera-vid", "--codec", "libav", "-o", "test.mp4", "-t", "8000", "--width", "640", "--height", "480"])
def preprocess_image(frame):
    resized_frame = cv2.resize(frame, (150, 150))
    grayscale_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    processed_frame = np.expand_dims(grayscale_frame, axis=-1)
    processed_frame = processed_frame / 255.0
    return processed_frame

def recognize_gesture(frame):
    input_data = preprocess_image(frame)
    input_data = np.expand_dims(input_data, axis=0)
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction)
    return predicted_class
cap=cv2.VideoCapture('test.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break
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

cap.release()
cv2.destroyAllWindows()

