import face_recognition
import os

def recognize_face(imgA,imgB):
    '''
    recognizes images
    '''
    known_image = face_recognition.load_image_file(imgA)
    unknown_image = face_recognition.load_image_file(imgB)

    know_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    # print(know_encoding)
    # print(unknown_encoding)
    results = face_recognition.compare_faces([know_encoding], unknown_encoding)
    return results

def empty_directory(directory):
    for file in os.listdir(directory):
        os.remove(os.path.join(directory, file))

# recognize_face('./faces/myimg.jpeg','./photos/8deb8144-d378-458d-a94a-f6ef513c89b2.jpeg')