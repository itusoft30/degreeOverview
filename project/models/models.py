from flask_sqlalchemy import SQLAlchemy
from project import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eihjewuminuans:a7c73a627a7488f86e19d477de45967dc9abd2e85591958438627d0cf4e275a0@ec2-54-247-96-169.eu-west-1.compute.amazonaws.com:5432/d2jv9l5jpv6eep'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Department(db.Model):
    __tablename__ = 'department'
    department_id = db.Column(db.Integer, primary_key=True)
    department_name = db.Column(db.String(50))
    faculty_name = db.Column(db.String(50))
    users = db.relationship('RegUser', backref="department")

    def __repr__(self):
        return f"department('{self.department_name}', '{self.faculty_name}')"

class RegUser(db.Model):
    __tablename__ = 'reguser'
    user_id = db.Column(db.Integer, primary_key=True)
    instructors = db.relationship('Instructor', back_populates="user")
    students = db.relationship('Student', back_populates="user")
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.Integer, default=0)
    department_id = db.Column(db.Integer, db.ForeignKey('department.department_id'))

    def __repr__(self):
        return f"reguser('{self.name}', '{self.surname}', '{self.email}', '{self.password}', '{self.usertype}'), '{self.department_id}"

class Instructor(db.Model):
    __tablename__ = 'instructor'
    instructor_id = db.Column(db.Integer, db.ForeignKey('reguser.user_id'))
    user = db.relationship('RegUser', back_populates="instructors")
    title = db.Column(db.String(50))
    courses = db.relationship('Course', back_populates="instructor")

    def __repr__(self):
        return f"instructor('{self.title}')"

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, db.ForeignKey('reguser.user_id'))
    user = db.relationship('RegUser', back_populates="students")
    id_number = db.Column(db.String(9))

    def __repr__(self):
        return f"department('{self.id_number}')"

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True)
    crn = db.Column(db.String(5))
    name = db.Column(db.String(50))
    course_code = db.Column(db.String(10))
    instructor_id = db.Column(db.Integer, db.ForeignKey('instructor.instructor_id'))
    instructor = db.relationship('Instructor', back_populates="courses")

    def __repr__(self):
        return f"department('{self.crn}', '{self.name}', '{self.course_code}', '{self.instructor_id}')"