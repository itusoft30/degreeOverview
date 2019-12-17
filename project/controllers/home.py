from project import app
from flask import render_template, redirect, url_for
"""
    Import MOdels
from project.models.Hello import Hello
"""
#route index
@app.route('/')
@app.route('/Home',methods= ['GET'])
def home():
    home_data = []
    return render_template('courses.html', data=home_data)

# @app.route('/changepassword', methods = ['POST'])
# def getProfile():
#     return ("changed password")