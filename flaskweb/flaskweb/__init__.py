"""
The flask application package.
"""

from flask import Blueprint, Flask

app = Flask(__name__)

# main = Blueprint('main', __name__, url_prefix='/')
# # 파일 이름이 index.py이므로
# from flaskweb.index import main as main
# app.register_blueprint(main)

from flaskweb.index import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/')

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404

