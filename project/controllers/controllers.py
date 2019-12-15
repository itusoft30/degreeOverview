from project import app
from flask import render_template, redirect, url_for
"""
    Import MOdels
from project.models.Hello import Hello
"""
#route index
@app.route('/', methods = ['GET'])
def index():
    return ("mainpage")

@app.route('/courses', methods = ['GET'])
def courses():
    coursesData = [] # get all courses from model
    departmentsData = [] # get all departments from model
    termsData = [] # get all terms from model
    return render_template('courses.html')

@app.route('/instructors', methods = ['GET'])
def instructors():
    instructorsData = {} # use model here to get instructors
    return render_template('instructors.html')


@app.route('/instructor/<instructorid>', methods = ['GET'])
def getInstructorWithID(instructorid):

    instructorData = 0 # Use model method here to get data with id <instructorid>

    # check if the instructor really exists

    return render_template('instructors.html', data = instructorData)

@app.route('/profile', methods = ['GET'])
def getProfile():
    userData = [] # get user data with logged in ID from model
    return ("my profile")


@app.route('/updateprofile', methods = ['POST'])
def updateProfile():
    return ("my profile updated")

# @app.route('/changepassword', methods = ['POST'])
# def getProfile():
#     return ("changed password")