from flask import Flask
from flaskweb import app

if __name__ == "__main__":
    app.secret_key = 'flaskweb'
    app.config['SESSION_TYPE'] = 'memcached'
    app.run(debug=True)