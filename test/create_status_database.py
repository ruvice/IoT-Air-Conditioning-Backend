from flask import Flask, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rssidatabase2.db'
# app.config['SECRET_KEY'] = 'secretKey'
db = SQLAlchemy(app)

# Class for Model to store in database
class StatusModel(db.Model):
    # Fields inside Video Model
    id = db.Column(db.Integer, primary_key=True)
    # Nullable means field cannot be null
    status = db.Column(db.Boolean, nullable=False)

    # Only when you want to print the representation of object
    def __repr__(self):
        return f"RSSI(id = {id}, status = {status})"

# Creates database
db.create_all()

rssi_entry = StatusModel(status=False)
db.session.add(rssi_entry)
db.session.commit()

result = StatusModel.query.filter_by(id=1).first()
print(result.status)

print("updating")
result.status = not result.status
db.session.add(result)
db.session.commit()
print(result.status)
