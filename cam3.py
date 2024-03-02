import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import time
from statistics import mode

import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import load_model

model = load_model('smnist.h5')

mphands = mp.solutions.hands
hands = mphands.Hands()
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

_, frame = cap.read()
h, w, c = frame.shape

letterpred = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

gesture_confidence_list = []

while True:
    start_time = time.time()
    while time.time() - start_time < 7:
        _, frame = cap.read()

        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape hit, closing...")
            break

        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(framergb)
        hand_landmarks = result.multi_hand_landmarks
        if hand_landmarks:
            for handLMs in hand_landmarks:
                x_max = 0
                y_max = 0
                x_min = w
                y_min = h
                for lm in handLMs.landmark:
                    x, y = int(lm.x * w), int(lm.y * h)
                    if x > x_max:
                        x_max = x
                    if x < x_min:
                        x_min = x
                    if y > y_max:
                        y_max = y
                    if y < y_min:
                        y_min = y
                y_min -= 20
                y_max += 20
                x_min -= 20
                x_max += 20
                cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

                analysisframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                analysisframe = analysisframe[y_min:y_max, x_min:x_max]
                analysisframe = cv2.resize(analysisframe, (28, 28))

                nlist = []
                rows, cols = analysisframe.shape
                for i in range(rows):
                    for j in range(cols):
                        k = analysisframe[i, j]
                        nlist.append(k)

                datan = pd.DataFrame(nlist).T
                colname = [val for val in range(784)]
                datan.columns = colname

                pixeldata = datan.values
                pixeldata = pixeldata / 255
                pixeldata = pixeldata.reshape(-1, 28, 28, 1)
                prediction = model.predict(pixeldata)
                predarray = np.array(prediction[0])
                predarrayordered = sorted(predarray, reverse=True)
                high1 = predarrayordered[0]

                gesture = letterpred[np.argmax(predarray)]
                confidence = high1

                gesture_confidence_list.append((gesture, confidence))

        cv2.imshow("Frame", frame)

    if gesture_confidence_list:
        gestures, confidences = zip(*gesture_confidence_list)
        main_gesture = mode(gestures)
        main_confidence = max(confidences)

        print("Main Predicted Gesture:", main_gesture)
        print("Main Confidence:", main_confidence)

    # Clear the list for the next iteration
    gesture_confidence_list = []

    if k % 256 == 27:
        break

cap.release()
cv2.destroyAllWindows()
