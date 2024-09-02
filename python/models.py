from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
    schedule = db.Column(db.String(255), nullable=False)  # e.g., "Monday 10:00-12:00"

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
