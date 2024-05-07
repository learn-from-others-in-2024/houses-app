from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
from dataclasses import dataclass
from flask_cors import CORS
from dataclasses import dataclass
import requests

app = Flask(__name__)
CORS(app)

# Specifying the database:
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://microservice:microservice@db/core'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Creating the House model:
@dataclass
class House(db.Model):
    id: int
    name: str
    image: str
    description: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(150))
    image = db.Column(db.String(150))
    description = db.Column(db.String(150))


# Creating the HouseChecker model:
@dataclass
class HouseChecker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checker_id = db.Column(db.Integer)
    house_id = db.Column(db.Integer)

    UniqueConstraint('checker_id', 'house_id', name='checker_house_unique')


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Request routing:


@app.route('/api/houses')
def index():
    return jsonify(House.query.all())


@app.route('/api/houses/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get(
        "'http://localhost:8000'/api/checker")
    json = req.json()

    try:
        houseChecker = HouseChecker(checker_id=json['id'], house_id=id)
        db.session.add(houseChecker)
        db.session.commit()

    except:
        abort(400, 'You have liked this house.')

    return jsonify({
        'message': 'success'
    })


@app.route('/api/houses/<int:id>/check', methods=['POST'])
def check(id):
    req = requests.get(
        "'http://localhost:8000'/api/checker")
    json = req.json()

    try:
        houseChecker = HouseChecker(checker_id=json['id'], house_id=id)
        db.session.add(houseChecker)
        db.session.commit()

    except:
        abort(400, 'You have checked this house.')

    return jsonify({
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
