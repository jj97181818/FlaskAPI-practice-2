from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                # Just return the dictionary. Do not need to use jsonify, because the flask_restful does it. 
                return item  
        # return null and add status code 404     
        return {"item": None}, 404
                

    def post(self, name):
        item = {"name": name, "price": 100}
        items.append(item)
        # return the item and the status code 201 which means the object has been successfully created
        return item, 201

api.add_resource(Item, '/item/<string:name>') 

app.run(port=5000)

