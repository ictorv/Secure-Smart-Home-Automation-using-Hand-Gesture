from transformers import pipeline
def gesture_recognizer(path):
    pipe = pipeline("image-classification", model="dima806/hand_gestures_image_detection")
    prediction = pipe(path)
    max_label = max(prediction, key=lambda x: x['score'])['label']
    return max_label