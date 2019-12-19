from project import app
from flask import render_template, redirect, url_for
from flask_login import login_required,current_user


@app.route('/UpdateInstructorProfile', methods = ['GET','POST'])
@login_required
def updateInstructor_Profile():
    print("burda")
    if(current_user.isInstructer() == False):
        print("home atayom")
        return redirect('Home')

    instructorData = 0 # Use model method here to get data with id <instructorid>

    # check if the instructor really exists

    return render_template('instructors.html', data = instructorData)
