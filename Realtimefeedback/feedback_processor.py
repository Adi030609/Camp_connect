import csv
from flask import request, jsonify

# Define the path for the CSV file where feedback will be stored
FEEDBACK_FILE = 'feedback_records.csv'

def process_feedback():
    """Process and save feedback submitted via the form."""
    try:
        # Extract form data
        feedback = request.form.get('feedback')
        user = request.form.get('user')

        if not feedback or not user:
            return jsonify({'success': False, 'message': 'Feedback and user information are required.'})

        # Append feedback to the CSV file
        with open(FEEDBACK_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user, feedback])

        return jsonify({'success': True, 'message': 'Feedback submitted successfully!'})

    except Exception as e:
        print(f"Error processing feedback: {e}")
        return jsonify({'success': False, 'message': 'An error occurred while processing your feedback.'})
