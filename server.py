import re
from flask import Flask, session, request, redirect, render_template, flash, url_for
from db.data_layer import get_user_by_email, get_user_by_id, create_user

app = Flask(__name__)
app.secret_key = '8118d0875ad5b6b3ad830b956b111fb0'

EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/authenticate')
def authenticate():
    return render_template('authenticate.html')

@app.route('/register', methods=['POST'])
def register():
    fullname = request.form['html_fullname']
    email = request.form['html_email']
    password = request.form['html_password']
    confirm = request.form['html_confirm']

    print('------------------------------')
    print(fullname, email, password, confirm)

    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    email = request.form['html_email']
    password = request.form['html_password']

    print('------------------------------')
    print(email, password)
    
    return redirect(url_for('index'))


app.run(debug=True)