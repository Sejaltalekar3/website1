from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'filesystem'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        name = request.form['Name']
        number = request.form['number']
        mail = request.form['mail']
        msg = request.form['msg']
        conn = sqlite3.connect('data.db')
        cursor= conn.cursor()
        cursor.execute('INSERT INTO contacts (Name, number, mail, msg) VALUES (?, ?, ?, ?)', (name, number, mail, msg))
        cursor.connection.commit()
        cursor.connection.close()
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
