from project import app
from flask import render_template, redirect, url_for
from project.controllers.forms import LoginForm
from project.config.crypto import Crypto
from project.models.models import RegUser

#route login
@app.route('/Login', methods = ['GET','POST'])
def Login():
    index_data = []
    form = LoginForm()
    if form.validate_on_submit():
        user = RegUser.query.filter_by(email=form.email.data+"@itu.edu.tr").first()
        if user.user_id and Crypto.checkPassword(form.password.data, user.password):
            print("girdi")

    return render_template('login.html',form=form, data=index_data,title='Login')