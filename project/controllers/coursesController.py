from project import app
from flask import render_template, redirect, url_for
from project.models.dbOperations import *

@app.route('/courses', methods = ['GET'])
def courses():
    coursesData = [] # get all courses from model
    departmentsData = [] # get all departments from model
    termsData = [] # get all terms from model
    return render_template('courses.html')


@app.route("/course/<int:course_id>")
def course(course_id):
    course = getCourseData(course_id)
    return render_template('course.html', course=course)