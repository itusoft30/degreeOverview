from flask import Flask, redirect, render_template,flash,url_for,current_app,request

from datetime import datetime
from urllib.parse import urlparse
import os


app = Flask(__name__)

@app.route('/')
def homepage():
    return ("Hello World!")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
