from project import app
from flask import render_template, redirect, url_for,flash
from flask_login import login_user, current_user, logout_user, login_required
from project.controllers.forms import LoginForm
from project.config.crypto import Crypto
from project.models.models import RegUser
from flask_login import login_user,current_user,logout_user,login_required

#route login
@app.route('/Login', methods = ['GET','POST'])
def Login():
    if current_user.is_authenticated:
        return(redirect(url_for('index')))
    index_data = []
    form = LoginForm()
    if form.validate_on_submit():
        user = RegUser.query.filter_by(email=form.email.data+"@itu.edu.tr").first()
        if user.user_id and Crypto.checkPassword(form.password.data, user.password):
            print("girdi")
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html',form=form, data=index_data,title='Login')

@app.route('/Logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))