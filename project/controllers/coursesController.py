from project import app
from flask import render_template, redirect, url_for
from project.models.dbOperations import *

@app.route('/courses', methods = ['GET'])
def courses():
    courses, courses_count = getAllCourses()
    return render_template('courses.html', courses=courses, courses_count=courses_count)

@app.route("/course/<int:course_id>")
def course(course_id):
    course = getCourseData(course_id)
    return render_template('course.html', course=course)