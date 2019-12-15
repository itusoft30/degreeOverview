from project import app
from flask import render_template, redirect, url_for

@app.route('/courses', methods = ['GET'])
def courses():
    coursesData = [] # get all courses from model
    departmentsData = [] # get all departments from model
    termsData = [] # get all terms from model
    return render_template('courses.html')