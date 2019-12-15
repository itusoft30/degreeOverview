from project import app
from flask import render_template, redirect, url_for

@app.route('/profile', methods = ['GET'])
def getProfile():
    userData = [] # get user data with logged in ID from model
    return ("my profile")


@app.route('/updateprofile', methods = ['POST'])
def updateProfile():
    return ("my profile updated")

# @app.route('/changepassword', methods = ['POST'])
# def getProfile():
#     return ("changed password"),