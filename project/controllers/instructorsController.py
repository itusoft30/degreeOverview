from project import app
from flask import render_template, redirect, url_for
from flask_login import login_required,current_user



@app.route('/instructors', methods = ['GET'])
def instructors():

    instructorData = 0 # Use model method here to get data with id <instructorid>

    # check if the instructor really exists

    return render_template('instructors.html', data = instructorData)
