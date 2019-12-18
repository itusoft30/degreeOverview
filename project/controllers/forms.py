from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from project.models.models import Course, Outcome, Department, RegUser


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

  
class RegistrationForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired(), Length(min=2, max=30)], render_kw={"placeholder": "First Name"})
    surname = StringField('Surname:', validators=[DataRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Last Name"})
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', 
                             validators=[DataRequired(),Length(min=5, max=10)], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "re-Password"})
    department = SelectField('Department:', validators=[DataRequired()], choices=[(dept.department_id, dept.department_name) for dept in Department.query], coerce= int, render_kw={"placeholder": "Department"})
    title = StringField('Title', validators=[Length(max=30)], render_kw={"placeholder": "Title"})
    student_no = StringField('Student No', validators=[Length(max=30)], render_kw={"placeholder": "Student Number"})
    submit = SubmitField('Sign Up')
    

class CourseRegistrationForm(FlaskForm):
    name = StringField('Course Name:', validators=[DataRequired(), Length(min=5, max=50)])
    crn = StringField('CRN:', validators=[DataRequired(), Length(min=5, max=5)])
    course_code = StringField('Course Code:',validators=[DataRequired(), Length(min=6, max=8)])
    credit = StringField('Credit:', validators=[DataRequired(), Length(min=1)])
    department = SelectField('Department:', validators=[DataRequired()], choices=[(dept.department_id, dept.department_name) for dept in Department.query], coerce= int)
    prerequisites = SelectMultipleField('Prerequisite/s:', choices=[(course.course_id, course.course_code) for course in Course.query], coerce= int)
    outcomes = SelectMultipleField('Outcome/s:', choices=[(out.outcome_id, out.name) for out in Outcome.query], coerce= int)
    submit = SubmitField('Submit')

class InstructorUpdateProfileForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired(), Length(min=2, max=30)])
    surname = StringField('Surname:', validators=[DataRequired(), Length(min=2, max=30)])
    title = StringField('Title:', validators=[DataRequired(), Length(min=3, max=50)])
    department = SelectField('Department:', validators=[DataRequired()], choices=[(dept.department_id, dept.department_name) for dept in Department.query], coerce= int)
    submit = SubmitField('Update profile')

class StudentUpdateProfileForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired(), Length(min=2, max=30)])
    surname = StringField('Surname:', validators=[DataRequired(), Length(min=2, max=30)])
    id_num = StringField('Student No:', validators=[DataRequired(), Length(min=8, max=9)])
    department = SelectField('Department:', validators=[DataRequired()], choices=[(dept.department_id, dept.department_name) for dept in Department.query], coerce= int)
    submit = SubmitField('Update profile')

class ChangePasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[DataRequired(),Length(min=6,max=10)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Change password')

class SearchForCourseForm():
    department = SelectField('Department:', validators=[DataRequired()], choices=[(dept.department_id, dept.department_name) for dept in Department.query], coerce= int)
    submit = SubmitField('Search')