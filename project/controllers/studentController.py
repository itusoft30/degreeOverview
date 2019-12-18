from project import app
from flask import render_template, redirect, url_for

@app.route('/UpdateStudentProfile', methods = ['GET'])
def updateStudent_Profile():
    return render_template('instructors.html')