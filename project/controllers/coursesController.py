from project import app
from flask import render_template, redirect, url_for, flash
from project.models.dbOperations import *
from flask_login import login_required, current_user
from project.controllers.forms import CourseRegistrationForm

@app.route('/courses', methods = ['GET'])
def courses():
    courses, courses_count = getAllCourses()
    return render_template('courses.html', courses=courses, courses_count=courses_count)

@app.route("/course/<int:course_id>")
def course(course_id):
    course = getCourseData(course_id)
    return render_template('course.html', course=course)

@app.route('/addCourse', methods = ['GET', 'POST'])
@login_required
def courseAdd():
    form = CourseRegistrationForm()
    if form.validate_on_submit():
        if registerCourse(form, current_user.user_id):
            flash('New course has been created!', 'success')
            return redirect(url_for('home'))
        else:
            flash('The email is already taken.')
    return render_template('courseAdd.html', form=form, title='Add a new course')