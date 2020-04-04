from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitor.db'

db = SQLAlchemy(app)

class Sites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    status = db.Column(db.String)

class snkrs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String)
    status = db.Column(db.String)

class best_buy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.String)
    name = db.Column(db.String)
    shipping = db.Column(db.String)
    instore = db.Column(db.String)

db.create_all()