from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

instructorsDB = [
    {
        'name': 'Ahmet Cüneyd Tantuğ',
        'faculty': 'Computer Engineering'},
    {
        'name': 'Hayri Turgut Uyar',
        'faculty': 'Computer Engineering'}
]
coursesDB = [
    {
        'code': 'BLG 105E',
        'name': 'Intro. to C Prog.',
        'prerequisites': ['BLG 101E', 'BLG 111E', 'BLG 111E', 'BLG 111E'],
        'outcomes': ['C Programming']},
    {
        'code': 'BLG 105E',
        'name': 'Intro. to C Prog.',
        'prerequisites': ['Computer Engineering'],
        'outcomes': ['C Programming']}
]

@app.route('/home')
def home():
    return render_template('rootHOME.html', title="home")

@app.route('/courses')
def courses():
    return render_template('rootCOURSES.html', title="courses", courses=coursesDB)

@app.route('/instructors')
def instructors():
    return render_template('rootINSTRUCTORS.html', title="instructors", instructors=instructorsDB)

@app.route('/profile')
def profile():
    return render_template('rootPROFILE.html', title="profile")

if __name__ == '__main__':
    app.run(debug=True)