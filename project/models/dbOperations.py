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


