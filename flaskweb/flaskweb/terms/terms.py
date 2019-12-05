from flask import Blueprint, request, render_template, Flask, flash, redirect, url_for, session
from flask import current_app as app
from datetime import datetime
import re
from flaskweb.module import dbModule

app = Flask(__name__)

terms_blueprint = Blueprint('terms', __name__, url_prefix='/')

@terms_blueprint.route('/list')
def list():
    print("#terms Redirect to home page ")
    return render_template('terms/list.html', username=session['username'])