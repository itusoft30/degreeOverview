from project import app
from flask import render_template, redirect, url_for
from flask_login import login_required

@app.route('/Profile', methods = ['GET'])
@login_required
def profile():
    userData = [] # get user data with logged in ID from model
    return render_template('profile.html')