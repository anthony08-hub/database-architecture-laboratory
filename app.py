from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="09633183975anthony08-",  
    database="notes_db"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    content = request.form['content']
    cursor.execute("INSERT INTO notes (content) VALUES (%s)", (content,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
