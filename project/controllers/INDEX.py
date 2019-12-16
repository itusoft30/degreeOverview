from project import app
from flask import render_template, redirect, url_for
"""
    Import MOdels
from project.models.Hello import Hello
"""
#route index
@app.route('/', methods = ['GET'])
def index():
    index_data = []
    return render_template('instructors.html', data=index_data)



# @app.route('/changepassword', methods = ['POST'])
# def getProfile():
#     return ("changed password")