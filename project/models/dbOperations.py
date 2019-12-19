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


def updateUserData(user_id, form):
    user = RegUser.query.get_or_404(user_id)
    user.name = form.name.data
    user.surname = form.surname.data
    user.department_id = form.department.data
    if user.user_type == 1:
        user.instructor.title = form.private_info.data
    else:
        user.student.id_number = form.private_info.data
    db.session.commit()
    return


def updateUserPassword(user_id, form):
    secret_password = Crypto.convertPassword(form.password.data)        # encrypting the password
    user = RegUser.query.get_or_404(user_id)                            # getting the user
    user.password = secret_password                                     # change the password in database
    db.session.commit()                                                 # commit
    return

   
def getCourseData(course_id):
    courseData = {}
    course = Course.query.get_or_404(course_id)
    courseData['course_code'] = course.course_code
    courseData['course_name'] = course.name
    courseData['department'] = Department.query.filter_by(department_id=course.department_id).first().department_name
    instructor_fullname = '%s %s' % (RegUser.query.filter_by(user_id=course.instructor_id).first().name, 
                                        RegUser.query.filter_by(user_id=course.instructor_id).first().surname)
    courseData['instructor'] = instructor_fullname
    courseData['crn'] = course.crn
    courseData['credit'] = course.credit

    prerequisite = ""
    requisite_ids = Prerequisite.query.filter_by(course_id=course_id)
    for _id in requisite_ids:
        prerequisite += Course.query.get_or_404(_id.requisite_id).course_code
        prerequisite += ", "
    prerequisite = prerequisite[:-2]
    if len(prerequisite) == 0 :
        prerequisite = "None"
    courseData['prerequisites'] = prerequisite

    outcome = ""
    outcome_ids = Course_Outcome.query.filter_by(course_id=course_id)
    for _id in outcome_ids:
        outcome += Outcome.query.get_or_404(_id.outcome_id).name
        outcome += ", "
    outcome = outcome[:-2]
    courseData['outcomes'] = outcome

    return courseData

