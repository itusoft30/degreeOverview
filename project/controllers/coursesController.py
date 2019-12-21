from project import app
from flask import render_template, redirect, url_for, flash, request
from project.models.dbOperations import *
from flask_login import login_required, current_user
from project.controllers.forms import CourseRegistrationForm, OutcomeRegistrationForm, StudentGradeForm,CourseUpdateForm

@app.route('/courses', methods = ['GET'])
def courses():
    courses, courses_count = getAllCourses()
    return render_template('courses.html', courses=courses, courses_count=courses_count)

@app.route("/course/<int:course_id>", methods = ['GET', 'POST'])
def course(course_id):
    editable = False
    course = getCourseData(course_id)
    studentGrade = GradeSetup(course_id)
    if course['insturctorId'] == current_user.user_id:
        editable = True
    form = StudentGradeForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            return redirect(url_for('Login'))
        if form.aa.data:
            addStudentGrade(current_user.user_id, course_id, 'AA')
        elif form.ba.data:
            addStudentGrade(current_user.user_id, course_id, 'BA')
        elif form.bb.data:
            addStudentGrade(current_user.user_id, course_id, 'BB')
        elif form.cb.data:
            addStudentGrade(current_user.user_id, course_id, 'CB')
        elif form.cc.data:
            addStudentGrade(current_user.user_id, course_id, 'CC')
        elif form.dc.data:
            addStudentGrade(current_user.user_id, course_id, 'DC')
        elif form.dd.data:
            addStudentGrade(current_user.user_id, course_id, 'DD')
        elif form.vf.data:
            addStudentGrade(current_user.user_id, course_id, 'VF')
        elif form.ff.data:
            addStudentGrade(current_user.user_id, course_id, 'FF')

    return render_template('course.html',edit = editable,form=form, course=course,course_id=course_id,student_grade=studentGrade)

@app.route('/addCourse', methods = ['GET', 'POST'])
@login_required
def courseAdd():
    if (current_user.isInstructor() == False):
        return redirect('home')
    form = CourseRegistrationForm()
    if form.validate_on_submit():
        if registerCourse(form, current_user.user_id):
            flash('New course has been created!', 'success')
            return redirect(url_for('home'))
        else:
            flash('The crn already exist.')
    return render_template('courseAdd.html', form=form, title='Add a new course')

@app.route('/editCourse/<int:course_id>', methods = ['GET', 'POST'])
@login_required
def courseEdit(course_id):
    if (current_user.isInstructor() == False):
        return redirect('home')
    course = getCourseData(course_id)
    form = CourseUpdateForm()
    if form.validate_on_submit():
        if updateCourseData(course_id, form):
            flash('Course edited!', 'success')
            return redirect(url_for('course',course_id= course_id))
        else:
            flash('Course can not edited.')
    return render_template('courseEdit.html', form=form, title='Edit the Course',course=course)

@app.route('/addOutcome', methods = ['GET', 'POST'])
@login_required
def outcomeAdd():
    form = OutcomeRegistrationForm()
    if form.validate_on_submit():
        if registerOutcome(form):
            flash('New outcome has been created!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('The email is already taken.')
    return render_template('outcomeAdd.html', form=form, title='Add a new outcome')

def GradeSetup(course_id):
    studentGrade = '-'
    if current_user.is_authenticated:
        studentGrade = getStudentGrade(current_user.user_id, course_id)
        if studentGrade is None:
            studentGrade = '-'
    return studentGrade