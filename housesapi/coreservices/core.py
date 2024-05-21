from datetime import datetime
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from flask_migrate import Migrate
from flask_cors import CORS
from dataclasses import dataclass
import requests
import os
from producer import publish
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
HOUSES_SERVICE_URL = os.getenv("HOUSES_SERVICE_URL")

db = SQLAlchemy()


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


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Specifying the database:
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://microservice:microservice@db/core'

    db.init_app(app)
    migrate = Migrate(app, db)

    # Request routing:
    @app.route('/')
    def home():
        return jsonify({
            'message': 'Hello from Core Service',
            'processedAt': datetime.now()
        })

    @app.route('/api/houses')
    def index():
        return jsonify(House.query.all())

    @app.route('/api/houses/<int:id>/like', methods=['POST'])
    def like(id):
        req = requests.get(f"{HOUSES_SERVICE_URL}/api/checker")
        json = req.json()

        try:
            houseChecker = HouseChecker(checker_id=json['id'], house_id=id)
            db.session.add(houseChecker)
            db.session.commit()

            publish('house_liked', id)
        except:
            abort(400, 'You have liked this house.')

        return jsonify({
            'message': 'success'
        })

    @app.route('/api/houses/<int:id>/check', methods=['POST'])
    def check(id):
        req = requests.get(f"{HOUSES_SERVICE_URL}/api/checker")
        json = req.json()

        try:
            houseChecker = HouseChecker(checker_id=json['id'], house_id=id)
            db.session.add(houseChecker)
            db.session.commit()

            publish('house_checked', id)
        except:
            abort(400, 'You have checked this house.')

        return jsonify({
            'message': 'success'
        })

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5005, debug=True)
