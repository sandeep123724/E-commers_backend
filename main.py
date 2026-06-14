import jsonify
from flask import Flask,request,jsonfiy
import  customer
import product
import order
from  validation import ValidationError

app= Flask(__name__)

@app.before_request
def setup_database():
    customer.init_customer_table()
    product.init_product_table()
    order.init_order_table()
@app.route('/customer',methods=['POST'])
def add_customer():
    data = request.json
    try:
        if not request.json:
            return jsonfiy({'error':'Missing json body'})
        required_fields = ['name','email','phone','city']
        if not all(field in data for field in required_fields):
            return jsonfiy({'error':'missing required field'}),400

@app.route('/product', methods=['POST'])
def add_product():
    data = request.json


    if not data:
      return jsonify({'error': 'Missing JSON body'}), 400


    required = ['name', 'category', 'price', 'stock']
    if not all(field in data for field in required):
       return jsonify({'error': 'Missing required fields'}), 400

    try:
        res = product.create_product(**data)
        return jsonify(res), 201

    except ValidationError as e:
            return jsonify({'error': str(e)}), 400

@app.route('/order', methods=['POST'])
def create_order():
    try:
        return jsonify(order.place_order(**request.json)), 201
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/order/<int:order_id>/status', methods=['PUT'])
def change_status(order_id):
    try:
        return jsonify(order.update_order_status(order_id, **request.json)), 200
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)


