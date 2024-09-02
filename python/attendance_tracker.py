import face_recognition
import pickle
import pandas as pd
from datetime import datetime

def mark_attendance(face_image_path):
    with open('face_encodings.pkl', 'rb') as f:
        known_face_encodings, known_face_names = pickle.load(f)

    # Load the image to recognize
    unknown_image = face_recognition.load_image_file(face_image_path)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    if unknown_encodings:
        for encoding in unknown_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Mark attendance
            mark_attendance_in_file(name)

def mark_attendance_in_file(name):
    try:
        df = pd.read_csv('../attendance_records.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Name', 'Date', 'Status'])

    today = datetime.now().strftime('%Y-%m-%d')
    if not ((df['Name'] == name) & (df['Date'] == today)).any():
        df = df.append({'Name': name, 'Date': today, 'Status': 'Present'}, ignore_index=True)
        df.to_csv('../attendance_records.csv', index=False)

# Example usage
mark_attendance('../images/samples/sample_image.jpg')
