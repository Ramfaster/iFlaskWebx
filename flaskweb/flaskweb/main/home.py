from flask import Blueprint, request, render_template, Flask, flash, redirect, url_for, session

app = Flask(__name__)

#main = Blueprint('main', __name__, url_prefix='/')

@app.route('/home')
def main():
    # Check if user is loggedin
    # if 'loggedin' in session:
    print("#1 : ", session['loggedin'])
    if session['loggedin']:
        # User is loggedin show them the home page
        return render_template('/main/home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('main.login'))