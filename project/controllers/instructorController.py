from project import app
from flask import render_template, redirect, url_for

@app.route('/instructors', methods = ['GET'])
def instructors():
    instructorsData = {} # use model here to get instructors
    return render_template('instructors.html')


@app.route('/instructor/<instructorid>', methods = ['GET'])
def getInstructorWithID(instructorid):

    instructorData = 0 # Use model method here to get data with id <instructorid>

    # check if the instructor really exists

    return render_template('instructors.html', data = instructorData)
