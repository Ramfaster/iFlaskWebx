"""
The flask application package.
"""

from flask import Blueprint, Flask
from flaskweb.index import main_blueprint
from flaskweb.terms.terms import terms_blueprint

app = Flask(__name__)

# 파일 이름이 index.py이므로
#from flaskweb.index import main as main
app.register_blueprint(main_blueprint)

#from flaskweb.terms import terms as terms
app.register_blueprint(terms_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404

