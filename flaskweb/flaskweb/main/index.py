from flask import Blueprint, request, render_template, Flask, flash, redirect, url_for, session
from flask import current_app as app
from datetime import datetime
import re

from flaskweb.module import dbModule

app = Flask(__name__)

main = Blueprint('main', __name__, url_prefix='/')

db_class = dbModule.Database()
posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': '첫 번째 포스트',
        'content': '첫 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-01', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': '두 번째 포스트',
        'content': '두 번째 포스트 내용입니다.',
        'date_posted': datetime.strptime('2018-08-03', '%Y-%m-%d')
    },
]

@main.route('/')
@main.route('/index')
def index():
    # Check if user is loggedin
    # if 'loggedin' in session:
    print("#1 : ", session['loggedin'])
    if session['loggedin']:
        # User is loggedin show them the home page
        return render_template('/main/home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('main.login'))

@main.route('/login',methods=['GET', 'POST'])
def login():
    print("#2 : ", session['loggedin'])
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']

        # Check if account_id exists using MySQL
        try:
            sql = "SELECT * FROM TB_USER WHERE user_id = '%s'"%(username)
            row = db_class.executeOne(sql)
        finally:
            print('Error')

        # If account_id exists in account_ids table in out database
        if row['USER_ID'] == username:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['user_id'] = row['USER_ID']
            session['username'] = row['NAME']
            # Redirect to home page
            return render_template('/main/home.html', posts=posts)
            #return 'Logged in successfully!'
        else:
            # account_id doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('/main/login.html', msg=msg)

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('main.login'))

# def main():
#     # Check if user is loggedin
#     # if 'loggedin' in session:
#     print("#1 : ", session['loggedin'])
#     if session['loggedin']:
#         # User is loggedin show them the home page
#         return render_template('/main/main.html', username=session['username'])
#     # User is not loggedin redirect to login page
#     return redirect(url_for('main.login'))

@main.route('/register',methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('/main/register.html', msg=msg)



@main.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('main.login'))

@main.route('/about')
def about():
    return render_template('/main/about.html', title='About')

