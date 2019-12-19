from project import app
from flask import render_template, redirect, url_for,flash, request
from flask_login import login_user, current_user, logout_user, login_required
from project.controllers.forms import LoginForm, RegistrationForm
from project.config.crypto import Crypto
from flask_login import login_user,current_user,logout_user,login_required
from project.models.models import RegUser, Department
from project.models.dbOperations import *

#route login
@app.route('/login', methods = ['GET','POST'])
def Login():
    if current_user.is_authenticated:
        return(redirect(url_for('home')))
    index_data = []
    form = LoginForm()
    if form.validate_on_submit():
        user = RegUser.query.filter_by(email=form.email.data+"@itu.edu.tr").first()
        if user and Crypto.checkPassword(form.password.data, user.password):
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


@app.route('/register', methods = ['GET','POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if register(form):
            flash('Your account has been created! You are now able to login.', 'success')
            return render_template('home.html', title='Home')
        else:
            flash('The email is already taken.')

    return render_template('register.html', form=form, title='Register')

