from flask_sqlalchemy import SQLAlchemy
from project import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eihjewuminuans:a7c73a627a7488f86e19d477de45967dc9abd2e85591958438627d0cf4e275a0@ec2-54-247-96-169.eu-west-1.compute.amazonaws.com:5432/d2jv9l5jpv6eep'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
