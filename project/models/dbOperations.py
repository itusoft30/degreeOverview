from project import login_manager
from project.models.models import *
from project.config.crypto import Crypto
from project.config.Database import db


def registerUser(form):
    secret_password = Crypto.convertPassword(form.password.data)
    user = RegUser.query.filter_by(email=form.email.data+"@itu.edu.tr").first()
    if not user:    # if the email is not taken, create the user
        type = 2 if len(form.title.data) == 0 else 1
        user = RegUser(name=form.name.data, surname=form.surname.data, 
                email=form.email.data+"@itu.edu.tr", password=secret_password, 
                user_type=type, department_id=form.department.data)
        db.session.add(user)
        db.session.commit()
        if type == 1:   # if new user is a instructor
            print(user.user_id)
            print(form.title.data)
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

def registerCourse(form, user_id):
    course = Course.query.filter_by(crn=form.crn.data).first()
    if not course:
        course = Course(crn=form.crn.data, name=form.name.data, course_code=form.course_code.data,
                        credit=form.credit.data, department_id=form.department.data, instructor_id=user_id)
        db.session.add(course)
        db.session.commit()
        for id in form.prerequisites.data:      # adding all the prerequisites
            prerequisite = Prerequisite(course_id=course.course_id, requsite_id=id)
            db.session.add(prerequisite)
            de.session.commit()
        for outcome_id in form.outcomes.data:   # adding all the outcomes
            course_outcome = Course_Outcome(course_id=course.course_id, outcome_id=outcome_id)
            db.session.add(course_outcome)
            db.session.commit()
        return True
    else:
        print("The CRN is already taken.")
        return False


def updateCourseData(course_id, form):
    course = Course.query.filter_by(crn=form.crn.data).first()
    updated_course = Course.query.get_or_404(course_id)
    if course.crn != updated_course.crn and course.crn == form.crn.data:
        print("CRN is already taken.")
        return False
    course.crn = form.crn.data
    course.name = form.name.data
    course.course_code = form.course_code.data
    course.credit = form.credit.data
    course.department_id = form.department.data

    i = 0
    outcomes = Course_Outcome.query.filter_by(course_id=course_id)
    for outcome in outcomes:
        print(outcome.outcome_id)
        print(form.outcomes.data[i])
        #outcome.outcome_id = form.outcomes.data[i]
        i += 1

    i = 0
    prerequisites = Prerequisite.query.filter_by(course_id=course_id)
    for prerequisite in prerequisites:
        prerequisite.requisite_id = form.prerequisites.data[i]
        i += 1

    return True


def registerOutcome(form):
    outcome = Outcome.query.filter_by(name=form.name.data).first()
    if not outcome:
        outcome = Outcome(name=form.name.data)
        db.session.add(outcome)
        db.session.commit()
    else:
        print("Outcome already exists.")
        return False


def getUserData(user_id):
    userData = {}
    user = RegUser.query.filter_by(user_id=user_id).first()
    userData['type'] = 'Instructor' if user.user_type == 1 else 'Student'
    userData['name'] = user.name
    userData['surname'] = user.surname
    userData['department'] = Department.query.filter_by(department_id=user.department_id).first().department_name

    if user.user_type == 1 :
        print(user.instructor.title)
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

def getPrerequisites(course_id):
    prerequisite = []
    requisite_ids = Prerequisite.query.filter_by(course_id=course_id)
    for _id in requisite_ids:
        requisite = {}
        requisite['course_id'] = _id.requisite_id
        requisite['name'] = Course.query.get_or_404(_id.requisite_id).course_code
        prerequisite.append(requisite.copy())
    return prerequisite

def getPrerequisitesAsString(course_id):
    prerequisite = ""
    requisite_ids = Prerequisite.query.filter_by(course_id=course_id)
    for _id in requisite_ids:
        prerequisite += Course.query.get_or_404(_id.requisite_id).course_code
        prerequisite += ", "
    prerequisite = prerequisite[:-2]
    return prerequisite


def getOutcomes(course_id):
    outcome = ""
    outcome_ids = Course_Outcome.query.filter_by(course_id=course_id)
    for _id in outcome_ids:
        outcome += Outcome.query.get_or_404(_id.outcome_id).name
        outcome += ", "
    outcome = outcome[:-2]
    return outcome


def getAllCourses():
    result_courses = []
    courseData = {}
    courses = Course.query.all()

    for course in courses:
        print(course.course_id)
        courseData['course_id'] = course.course_id
        courseData['code'] = course.course_code

        prerequisites = getPrerequisitesAsString(course.course_id)
        courseData['prerequisites'] = prerequisites
        
        outcomes = getOutcomes(course.course_id)
        courseData['outcomes'] = outcomes

        result_courses.append(courseData.copy())
    return result_courses, len(courses)

def getInstructorFullName(instructor_id):
    return '%s %s' % (RegUser.query.filter_by(user_id=instructor_id).first().name, 
                                        RegUser.query.filter_by(user_id=instructor_id).first().surname)

   
def getCourseData(course_id):
    courseData = {}
    course = Course.query.get_or_404(course_id)
    courseData['course_code'] = course.course_code
    courseData['course_name'] = course.name
    courseData['department'] = Department.query.filter_by(department_id=course.department_id).first().department_name
    courseData['instructor'] = getInstructorFullName(course.instructor_id)
    courseData['crn'] = course.crn
    courseData['credit'] = course.credit
    courseData['prerequisites'] = getPrerequisites(course_id)
    courseData['outcomes'] = getOutcomes(course_id)

    return courseData

def getCourse(course_id):
    return Course.query.get_or_404(course_id)


def getPrerequisitesIds(course_id):
    prerequisites = Prerequisite.query.filter_by(course_id=course_id)
    prerequisite_ids = []
    for _id in prerequisites:
        prerequisite_ids.append((_id.requisite_id))

    return prerequisite_ids


def getOutcomeIds(course_id):
    outcomes = Course_Outcome.query.filter_by(course_id=course_id)
    outcome_ids = []
    for _id in outcomes:
        outcome_ids.append((_id.outcome_id))

    return outcome_ids


def getAllInstructors():
    result_instructors = []
    instructorData = {}
    instructors = Instructor.query.all()
    for instructor in instructors:
        instructorData['instructor_id'] = instructor.instructor_id
        instructorData['name'] = getInstructorFullName(instructor.instructor_id)
        department_id = RegUser.query.filter_by(user_id=instructor.instructor_id).first().department_id
        instructorData['faculty'] = Department.query.filter_by(department_id=department_id).first().faculty_name

        result_instructors.append(instructorData.copy())

    return result_instructors, len(instructors)

def getInstructorData(instructor_id):
    instructorData = {}
    instructor = Instructor.query.get_or_404(instructor_id)
    instructorData['name'] = getInstructorFullName(instructor_id)
    instructorData['title'] = instructor.title
    userData = RegUser.query.get_or_404(instructor_id)
    instructorData['email'] = userData.email
    instructorData['department'] = Department.query.filter_by(department_id=userData.department_id).first().department_name
    courseData = {}
    final_courses = []
    for course in instructor.courses:
        courseData['course_id'] = course.course_id
        courseData['code'] = course.course_code
        courseData['prerequisites'] = getPrerequisites(course.course_id)
        courseData['outcomes'] = getOutcomes(course.course_id)

        final_courses.append(courseData.copy())

    instructorData['courses'] = final_courses
    instructorData['course_count'] = len(instructor.courses)

    return instructorData

def getStudentGrade(user_id, course_id):
    studentGrade = Student_Grade.query.filter_by(student_id=user_id, course_id=course_id).first()
    if studentGrade is None:
        return None
    else:
        return studentGrade.grade

def addStudentGrade(user_id, course_id, grade):
    studentGrade = Student_Grade.query.filter_by(student_id=user_id, course_id=course_id).first()
    if not studentGrade:
        studentGrade = Student_Grade(student_id=user_id, course_id=course_id, grade=grade)
        db.session.add(studentGrade)
    else:
        print(grade)
        studentGrade.grade = grade
    db.session.commit()
    return
