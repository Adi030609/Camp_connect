from flask import Flask, render_template, request, redirect, url_for
import os
from attendance_tracker import mark_attendance

app = Flask(__name__, template_folder='../html')

UPLOAD_FOLDER = '../images/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        mark_attendance(filepath)
        return redirect(url_for('attendance'))

@app.route('/attendance')
def attendance():
    try:
        with open('../attendance_records.csv', 'r') as f:
            attendance_data = f.read()
    except FileNotFoundError:
        attendance_data = "No attendance records found."

    return render_template('attendance.html', data=attendance_data)

if __name__ == "__main__":
    app.run(debug=True)
