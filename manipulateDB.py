import sqlite3
from flask import Flask

app = Flask(__name__)
db_connection = sqlite3.connect("lerningDatabase.db")

db_cursor = db_connection.cursor()

# db_cursor.execute('select * from Courses')
# students = db_cursor.fetchall()

db_connection.execute('CREATE TABLE IF NOT EXISTS Courses ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT NOT NULL, instructor TEXT not null, preReq TEXT not null)')

db_cursor.execute('insert into Courses (name, description, instructor, preReq) values (?, ?, ?, ?)', ('Mathematics', 'Algebra, Calculus, Trigonometry, Statistics', 'Alice First', 'Basic mathematics'))
db_cursor.execute('insert into Courses (name, description, instructor, preReq) values (?, ?, ?, ?)', ('Computer Science', 'Leran Tech Languages from the experts', 'Kennedy John', 'Basic computer skills'))
db_cursor.execute('insert into Courses (name, description, instructor, preReq) values (?, ?, ?, ?)', ('Science', 'Learn environment', 'Abraham Lincon', 'None'))
db_cursor.execute('insert into Courses (name, description, instructor, preReq) values (?, ?, ?, ?)', ('Physics', 'Fluid  Mechanics, Thermo Dynamics, Kinematics, Force', 'John cena', 'Basic mathematics'))
db_cursor.execute('insert into Courses (name, description, instructor, preReq) values (?, ?, ?, ?)', ('Biology', 'Photosynthesis, , Cells, Organisms, Reproduction', 'Mary Cury ', 'None'))
db_cursor.execute('insert into Courses (name, description, instructor, preReq) values (?, ?, ?, ?)', ('Chemistry', 'Analytical Chemistry, Electrochemistry, Inorganic Chemistry, Organic Chemistry, ', 'Anand Vihari', 'None'))
db_cursor.execute('select * from Courses')
students = db_cursor.fetchall()

print(f' Students :  {students}')