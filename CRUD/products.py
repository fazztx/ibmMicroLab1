from flask import Flask, jsonify, redirect, request
import json
from flask_cors import CORS

app = Flask("Product Server") #REST APIs for adding, retrieving, updating, and deleting product
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

#
#Add all the REST API end-points here
#
@app.route('/', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/product/<int:id>', methods=['GET'])
def get_exact_product(id):
    #id = int(id) 
    for eachProduct in products:
        if eachProduct.get("id") == id:
            return jsonify(eachProduct)
    return jsonify({"error":'Not found'}), 404

@app.route('/', methods=['POST'])
def add_product():
    product =  request.get_json() # Able to receive JSON from body
    products.append(product)
    return jsonify({"success":'Added'}), 201 #REST API
    #return redirect('/') #Route to the first method #WebAPI

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    id = int(id) 
    for eachProduct in products:
        if eachProduct.get("id") == id:
            eachProduct["name"] = request.get_json().get("name")
            eachProduct["price"] = request.get_json().get("price")
            return jsonify({"success":'Updated'}), 200
    return jsonify({"message":'Nothing to update'}), 200

@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    id = int(id)
    product = next((x for x in products if x["id"] == id), None)
    if product:
        products.remove(product)
        return 'Deleted', 204
    return jsonify({'error': 'Product not found'}), 404 #REST API
    #return redirect('/') #Route to the first method



# app.run(port=5000,debug=True)
