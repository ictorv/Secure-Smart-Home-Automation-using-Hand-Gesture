import cv2
import face_recognition

known_image = face_recognition.load_image_file("obama.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

cap = cv2.VideoCapture(0)
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Compare each face encoding with the known face encoding
    for face_encoding in face_encodings:
        # Compare the current face encoding with the known face encoding
        match = face_recognition.compare_faces([known_encoding], face_encoding)

        # If a match is found, label the face
        if match[0]:
            cv2.putText(frame, "Known Face", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cap.release()
            cv2.destroyAllWindows()

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
# cv2.destroyAllWindows()