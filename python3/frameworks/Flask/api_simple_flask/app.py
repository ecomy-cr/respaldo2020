from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)

from data import MyData

# Testing Route
@app.route('/', methods=['GET'])
def test():
    return jsonify({'response': 'test!'})

# Get Data Routes
@app.route('/MyData')
def obtener_productos():
    # return jsonify(MyData)
    return jsonify({'MyData': MyData})


@app.route('/MyData/<string:pk>', methods=['GET'])
def obtener_producto(pk):
    print('este el que envio por post: ->' + pk)
    for i in MyData:
        vari = str(i['name'].lower())
        
        if vari == pk:
            return jsonify({'product': i})
        
    return jsonify({'message': 'Product Not found'})


# Create Data Routes
@app.route('/MyData', methods=['POST'])
def agregar_nuevo_producto():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 103
    }
    MyData.append(new_product)
    return jsonify({'MyData': MyData})

# Update Data Route
@app.route('/MyData/<string:pk>', methods=['PUT'])
def editar_producto(pk):
    
    print('este el que envio por post: ->' + pk)
    for i in MyData:
        vari = str(i['name'].lower())
        
        if vari == pk:
            
            name = request.json['name']
            price = request.json['price']
            quantity = request.json['quantity']
            data = {
                'name': name,
                'price':price,
                'quantity' :quantity
            }
            #actualizo datos en db o archivos etc, en otro repositorio se explico el caso.
            return jsonify({
                'message': 'Product Updated',
                'product': data
            })
        
    return jsonify({'message': 'Product Not found'})

if __name__ == '__main__':
    app.run(debug=True, port=3444)
