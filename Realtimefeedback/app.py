
from flask import Flask, request, redirect, url_for
from feedback_processor import process_feedback
from feedback_viewer import view_feedback

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('view_feedback'))

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    return process_feedback()

@app.route('/view-feedback')
def feedback_view():
    return view_feedback()

if __name__ == '__main__':
    app.run(debug=True)
