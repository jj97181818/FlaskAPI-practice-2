from flask import Flask, request
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
        # If set force = True, it will not check the header of request and do the processing even it's not correct
        # data = request.get_json(force=True)
        # If set silent = True, it will not send errors but returns none.
        # data = request.get_json(silent=True)
        data = request.get_json()
        item = {"name": name, "price": data['price']}
        items.append(item)
        # return the item and the status code 201 which means the object has been successfully created
        return item, 201

class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')

# run the app and get the error message
app.run(port=5000, debug=True)

