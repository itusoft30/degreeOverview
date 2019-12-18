from project import app
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from project.models.models import RegUser, Department
from project.models.dbOperations import *


@app.route('/Profile', methods = ['GET'])
@login_required
def profile():
    userData = getUserData(current_user.user_id)
    return render_template('profile.html', user=userData, title='Profile')