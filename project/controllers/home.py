from project import app
from flask import render_template, redirect, url_for
"""
    Import MOdels
from project.models.Hello import Hello
"""
#route index
@app.route('/')
@app.route('/Home', methods= ['GET'])
def Home():
    home_data = []
    return render_template('rootHOME.html', data=home_data, title='Home')

# @app.route('/changepassword', methods = ['POST'])
# def getProfile():
#     return ("changed password")