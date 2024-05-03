from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

core = Flask(__name__)

CORS(core)

# Specifying the database:
core.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://microservice:microservice@db/core'

db = SQLAlchemy(core)

@core.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    core.run(host='0.0.0.0', port=5005, debug=True)
