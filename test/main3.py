from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rssidatabase2.db'
db = SQLAlchemy(app)

# Class for Model to store in database
class RSSIModel(db.Model):
    # Fields inside Video Model
    id = db.Column(db.Integer, primary_key=True)
    # Nullable means field cannot be null
    beacon1 = db.Column(db.Integer, nullable=False)
    beacon2 = db.Column(db.Integer, nullable=False)
    beacon3 = db.Column(db.Integer, nullable=False)
    location = db.Column(db.Integer, nullable=False)

    # Not supported by python version on azure
    # Only when you want to print the representation of object
    # def __repr__(self):
    #     return f"RSSI(id = {id}, beacon1 = {beacon1}, beacon2 = {beacon2}, beacon3 = {beacon3})"

# Creates database
# db.create_all()
rssi_get_args = reqparse.RequestParser()
rssi_get_args.add_argument("beacon1", type=int, help="RSSI Value of Beacon 1", required=True)
rssi_get_args.add_argument("beacon2", type=int, help="RSSI Value of Beacon 2", required=True)
rssi_get_args.add_argument("beacon3", type=int, help="RSSI Value of Beacon 3", required=True)
# rssi_get_args.add_argument("location", type=int, help="Location ID", required=True)


rssi_put_args = reqparse.RequestParser()
rssi_put_args.add_argument("beacon1", type=int, help="RSSI Value of Beacon 1", required=True)
rssi_put_args.add_argument("beacon2", type=int, help="RSSI Value of Beacon 2", required=True)
rssi_put_args.add_argument("beacon3", type=int, help="RSSI Value of Beacon 3", required=True)
rssi_put_args.add_argument("location", type=int, help="Location ID", required=True)


# locations
# 0 - hall
# 1 - room
# 2 - corridor
# 3 - lift
resource_fields = {
    'id': fields.Integer,
    'beacon1': fields.Integer,
    'beacon2': fields.Integer,
    'beacon3': fields.Integer,
    'location': fields.Integer,
}

get_resource_fields = {
    'location': fields.Integer,
}

# load the knn model from disk
loaded_model = pickle.load(open('knnpickle_file', 'rb'))

# Makes a class that inherits from Resource
class Classify(Resource):
    # @marshal_with(get_resource_fields)
    def get(self):
        args = rssi_get_args.parse_args()

        example_measures = np.array([[args["beacon1"],args["beacon2"],args["beacon3"]]])
        example_measures = example_measures.reshape(len(example_measures), -1)
        result = loaded_model.predict(example_measures)
        resultJSON = json.dumps(result.tolist())
        print(resultJSON)
        return resultJSON

    @marshal_with(resource_fields)
    def put(self):
        args = rssi_put_args.parse_args()
        
        rssi_entry = RSSIModel(beacon1=args['beacon1'], beacon2=args['beacon2'], beacon3=args['beacon3'], location=args['location'])
        db.session.add(rssi_entry)
        db.session.commit()
        return rssi_entry, 201 # Status code

# api.add_resource(Classify, "/classify/<int:rssi_id>")
api.add_resource(Classify, "/classify/")

if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0')
    app.run(host='0.0.0.0')
    