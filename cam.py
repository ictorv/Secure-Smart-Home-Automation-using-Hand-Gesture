import random
import time

import cv2
import numpy as np
from skimage.transform import resize
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('model.h5')  
# Dictionary to map class indices to gesture names (A-Z)
gesture_names = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 
    18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y'
}


def preprocess_image(image, filename):

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Apply background removal (e.g., using thresholding)
    #_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite(filename,gray_image)
    # Resize the image to match the input size expected by the model
    resized_image = cv2.resize(gray_image, (28, 28), interpolation=cv2.INTER_AREA)
    
    # Normalize the image
    normalized_image = resized_image / 255.0
    
    # Reshape the image to match the input shape expected by the model
    processed_image = normalized_image.reshape(-1, 28, 28, 1)
    
    return processed_image

def predict_gesture(image):
    # Preprocess the image (resize, normalize, etc.)
    processed_image = preprocess_image(image,'test1.jpg')
    
    # Make prediction
    prediction = model.predict(processed_image)
    
    # Get the predicted gesture class index
    predicted_class = np.argmax(prediction)
    
    # Map the class index to gesture name
    gesture_name = gesture_names.get(predicted_class, 'Unknown')
    
    return gesture_name
def predict_from_image():
    image = cv2.imread('test2.jpg') 

    print(predict_gesture(image))

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    # Initialize list to store frames
    frames = []
    start_time = time.time()
    while time.time() - start_time <= 7:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Display the captured frame
        cv2.imshow('Webcam', frame)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Append the captured frame to the list
        frames.append(frame)
    
    
    # Select a frame for prediction 
    if frames:
        random_index = random.randint(0, len(frames) - 1)
        selected_frame = frames[random_index]
        
        # Preprocess the selected frame and make a prediction
        gesture = predict_gesture(selected_frame)
        cv2.putText(frame, f'Predicted Gesture: {gesture}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        # Display the predicted gesture
        print('Predicted Gesture:', gesture)
    # Release the webcam
    cap.release()
    # Close all OpenCV windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    #predict_from_image()
