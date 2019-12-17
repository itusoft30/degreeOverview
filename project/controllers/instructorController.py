from project import app
from flask import render_template, redirect, url_for



@app.route('/UpdateInstructorProfile', methods = ['GET'])
def updateInstructor_Profile():

    instructorData = 0 # Use model method here to get data with id <instructorid>

    # check if the instructor really exists

    return render_template('instructors.html', data = instructorData)
