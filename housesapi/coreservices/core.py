from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dataclasses import dataclass
from flask_cors import CORS

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


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
