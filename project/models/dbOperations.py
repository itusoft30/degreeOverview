from project import login_manager
from project.models.models import *
from project.config.crypto import Crypto
from project.config.Database import db


def register(form):
    secret_password = Crypto.convertPassword(form.password.data)
    user = RegUser.query.filter_by(email=form.email.data+"@itu.edu.tr").first()
    if not user:    # if the email is not taken, create the user
        type = 2 if len(form.title.data) == 0 else 1
        user = RegUser(name=form.name.data, surname=form.surname.data, 
                email=form.email.data+"@itu.edu.tr", password=secret_password, 
                user_type=type, department_id=form.department.data)
        db.session.add(user)
        db.session.commit()
        print(user.user_id)
        if type == 2:   # if new user is a instructor
            instructor = Instructor(instructor_id=user.user_id, title=form.title.data)
            db.session.add(instructor)
            db.session.commit()
        else:           # otherwise, the user is a student
            student = Student(student_id=user.user_id, id_number=form.student_no.data)
            db.session.add(student)
            db.session.commit()
        return True
    else:
        print("The email is already taken.")
        return False

def getUserData(user_id):
    userData = {}
    user = RegUser.query.filter_by(user_id=user_id).first()
    userData['type'] = 'Instructor' if user.user_type == 1 else 'Student'
    userData['name'] = user.name
    userData['surname'] = user.surname
    userData['department'] = Department.query.filter_by(department_id=user.department_id).first().department_name

    if user.user_type == 1 :
        userData['private_info'] = user.instructor.title
    else:
        userData['private_info'] = user.student.id_number

    userData['email'] = user.email
    
    return userData


