"""
The flask application package.
"""

from flask import Flask

app = Flask(__name__)

# # 파일 이름이 index.py이므로
from flaskweb.main.index import main as main

app.register_blueprint(main)