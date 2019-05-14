from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'Jane'
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        # filter return filter object
        # list() convert the filter object to list
        # next() give the first item found in filter function. 
        # If you call next() again, you will get the second item, and so on.
        # If there is no item matched, return None
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"item": None}, 200 if item else 404
        # 200 if item is not None else 404
                

    def post(self, name):
        # if there exists an item matched, and return is not None
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message": "An item with name '{}' already exists.".format(name)}, 400 
        data = request.get_json()
        item = {"name": name, "price": data['price']}
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')

# run the app and get the error message
app.run(port=5000, debug=True)

