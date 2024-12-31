import cv2
import face_recognition
import os
import numpy as np


# Step 1: Load the dataset
def load_dataset(dataset_path):
    known_encodings = []
    known_names = []

    for person_name in os.listdir(dataset_path):
        person_path = os.path.join(dataset_path, person_name)
        if os.path.isdir(person_path):
            for image_name in os.listdir(person_path):
                image_path = os.path.join(person_path, image_name)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)
                if encodings:
                    known_encodings.append(encodings[0])
                    known_names.append(person_name)
    return known_encodings, known_names


dataset_path = 'path to your dataset'
known_encodings, known_names = load_dataset(dataset_path)

video_capture = cv2.VideoCapture(0)

while True:
    result, video_frame = video_capture.read()
    if not result:
        break

    rgb_frame = cv2.cvtColor(video_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        if len(face_distances) > 0 and matches:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]

        cv2.rectangle(video_frame, (left, top), (right, bottom), (0, 255, 0), 4)
        cv2.putText(
            video_frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2,
        )

    cv2.imshow("Face Recognition", video_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
