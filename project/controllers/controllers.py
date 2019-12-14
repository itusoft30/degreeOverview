from project import app
from flask import render_template, redirect, url_for
"""
    Import MOdels
from project.models.Hello import Hello
"""
#route index
@app.route('/', methods = ['GET'])
def index():
    return "home"


@app.route('/courses', methods = ['GET'])
def courses():
    return ("courses page")

@app.route('/instructors', methods = ['GET'])
def instructors():
    return ("instructors")


@app.route('/instructor/<instructorid>', methods = ['GET'])
def getInstructor(instructorid):
    return ("instructor with id : %s" % instructorid)