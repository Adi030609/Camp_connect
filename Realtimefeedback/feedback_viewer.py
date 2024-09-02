import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/view-feedback')
def view_feedback():
    try:
        # Load feedback records from CSV
        feedback_data = pd.read_csv('feedback_records.csv')
    except FileNotFoundError:
        feedback_data = pd.DataFrame(columns=['Name', 'Feedback'])
    
    # Convert DataFrame to HTML
    feedback_html = feedback_data.to_html(classes='table table-striped', index=False)
    
    return render_template('view_feedback.html', feedback_html=feedback_html)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
