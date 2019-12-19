from project import app
from flask import render_template, redirect, url_for
from flask_login import login_required,current_user

@app.route('/UpdateStudentProfile', methods = ['GET'])
@login_required
def updateStudent_Profile():
    print("--->",current_user.user_type)
    print(current_user.isStudent())
    if (current_user.isStudent() == False):
        return redirect('home')

    return render_template('profile.html')