from flask import Flask, render_template, request, redirect, url_for
import sqlite3
ta_username="aaaa"
ta_password="1234"
app = Flask(__name__)

def get_student_score(username, password):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT score FROM students WHERE student_name=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        score = get_student_score(username, password)
        if score:
            return render_template('result.html', name=username, score=score[0])
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
