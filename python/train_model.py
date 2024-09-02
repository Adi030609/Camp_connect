import face_recognition
import os
import pickle

def train_model():
    known_face_encodings = []
    known_face_names = []

    # Specify the correct directory path
    samples_dir = 'C:/Users/adity/OneDrive/Desktop/Camp_connect/images/sample'

    # Loop through all the files in the samples directory
    for filename in os.listdir(samples_dir):
        # Construct the full file path
        file_path = os.path.join(samples_dir, filename)

        # Load the image and get the face encoding
        image = face_recognition.load_image_file(file_path)
        encodings = face_recognition.face_encodings(image)
        
        if encodings:  # Check if there is at least one face encoding found
            encoding = encodings[0]
            known_face_encodings.append(encoding)
            # Use the filename (without extension) as the name
            known_face_names.append(os.path.splitext(filename)[0])

    # Save the known face encodings and names to a pickle file
    with open('face_encodings.pkl', 'wb') as f:
        pickle.dump((known_face_encodings, known_face_names), f)

if __name__ == "__main__":
    train_model()
