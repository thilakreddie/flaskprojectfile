from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app = Flask(__name__)
db_connection = sqlite3.connect("lerningDatabase.db")
db_connection.execute('CREATE TABLE IF NOT EXISTS Student ( id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)')
db_connection.execute('CREATE TABLE IF NOT EXISTS Courses ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT NOT NULL, instructor TEXT not null, preReq TEXT not null)')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services", methods=["GET", "POST"])
def services():
    if request.method == 'GET':
        db_connection = sqlite3.connect("lerningDatabase.db")
        db_cursor = db_connection.cursor()
        db_cursor.execute('SELECT * from Courses')
        db_cursor.execute
        courses = db_cursor.fetchall()
        return render_template("services.html", courses = courses)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error_message = ''
    if request.method == 'POST':
        uname = request.form['uname']
        psw = request.form['psw']
        if not uname or not psw:
            error_message = 'Please fill out all the fields'
        elif len(psw) <= 8:
            error_message = 'Password should be minimum of length 8'
        if error_message == '': 
            db_connection = sqlite3.connect("lerningDatabase.db")
            db_cursor = db_connection.cursor()
            db_cursor.execute('SELECT * FROM Student WHERE username = ? and password = ?', (uname,psw))
            user_account = db_cursor.fetchone()
            if user_account:
                error_message = 'Sucessfully logged in'
                return render_template('index.html')
            else:
                error_message = 'Invalid Username/Password'
                return render_template('login.html', login_errors = error_message)
    return render_template("login.html", login_errors = error_message)

@app.route("/registration", methods=["GET", "POST"])
def registration():
    error_message = ''
    if request.method == 'POST':
        uname = request.form['uname']
        psw = request.form['psw']
        cpsw = request.form['cpsw']
        if not uname or not psw or not cpsw:
            error_message = 'Please fill out all the fields'
        elif len(psw) <= 8:
            error_message = 'Password should be minimum of length 8'
        elif not psw == cpsw:
            error_message = 'password and confirm password must be same' 
        if error_message == '': 
            db_connection = sqlite3.connect("lerningDatabase.db")
            db_cursor = db_connection.cursor()
            db_cursor.execute('SELECT * FROM Student WHERE username = ?', (uname,))
            db_cursor.execute('insert into Courses (name, description, instructor, preReq) values (?, ?, ?, ?)', ('Biology', 'Photosynthesis, , Cells, Organisms, Reproduction', 'Mary Cury ', 'None'))
            user_account = db_cursor.fetchone()
            if user_account:
                error_message = 'Account already exists with the same username !'
            else:
                db_cursor.execute('INSERT INTO Student (username, password) VALUES (?, ?)', (uname, psw ))
                db_cursor.execute('insert into Courses (name, description, instructor, preReq) values (?, ?, ?, ?)', ('Chemistry', 'Analytical Chemistry, Electrochemistry, Inorganic Chemistry, Organic Chemistry, ', 'Anand Vihari', 'None'))
                db_connection.commit()
                error_message = 'Successfully registered!'
                return render_template('index.html')
    return render_template("register.html", registration_errors = error_message)

@app.route('/students')
def students():
    db_connection = sqlite3.connect("lerningDatabase.db")
    db_connection.row_factory = sqlite3.Row

    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * FROM Student")

    rows = db_cursor.fetchall();
    return render_template("students.html", rows=rows)

@app.route('/courses')
def courses():
    db_connection = sqlite3.connect("lerningDatabase.db")
    db_connection.row_factory = sqlite3.Row

    db_cursor = db_connection.cursor()
    db_cursor.execute("SELECT * FROM Courses")

    rows = db_cursor.fetchall();
    return render_template("courseList.html", rows=rows)