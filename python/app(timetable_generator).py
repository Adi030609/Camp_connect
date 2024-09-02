from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timetable.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# Define models
class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return f'<Faculty {self.name}>'

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)
    schedule = db.Column(db.String(255), nullable=False)

    faculty = db.relationship('Faculty', backref=db.backref('courses', lazy=True))

    def __repr__(self):
        return f'<Course {self.name} - {self.faculty.name}>'

class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    course = db.relationship('Course', backref=db.backref('timetables', lazy=True))

    def __repr__(self):
        return f'<Timetable {self.course.name} on {self.date} at {self.time}>'

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_faculty', methods=['GET', 'POST'])
def add_faculty():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if name and email:
            new_faculty = Faculty(name=name, email=email)
            db.session.add(new_faculty)
            db.session.commit()
            flash('Faculty added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('All fields are required!', 'error')
    return render_template('add_faculty.html')

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        faculty_id = request.form['faculty_id']
        schedule = request.form['schedule']
        if name and faculty_id and schedule:
            new_course = Course(name=name, faculty_id=faculty_id, schedule=schedule)
            db.session.add(new_course)
            db.session.commit()
            flash('Course added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('All fields are required!', 'error')
    faculties = Faculty.query.all()
    return render_template('add_course.html', faculties=faculties)

@app.route('/add_timetable', methods=['GET', 'POST'])
def add_timetable():
    if request.method == 'POST':
        course_id = request.form['course_id']
        date = request.form['date']
        time = request.form['time']
        if course_id and date and time:
            new_timetable = Timetable(course_id=course_id, date=datetime.strptime(date, '%Y-%m-%d').date(), time=datetime.strptime(time, '%H:%M').time())
            db.session.add(new_timetable)
            db.session.commit()
            flash('Timetable entry added successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('All fields are required!', 'error')
    courses = Course.query.all()
    return render_template('add_timetable.html', courses=courses)

@app.route('/view_timetable')
def view_timetable():
    timetables = Timetable.query.order_by(Timetable.date, Timetable.time).all()
    return render_template('view_timetable.html', timetables=timetables)

if __name__ == '__main__':
    app.run(debug=True)
