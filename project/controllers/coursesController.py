from project import app
from flask import render_template, redirect, url_for
from flask_login import login_required

@app.route('/courses', methods = ['GET'])
@login_required
def courses():
    coursesData = [] # get all courses from model
    departmentsData = [] # get all departments from model
    termsData = [] # get all terms from model
    return render_template('courses.html')