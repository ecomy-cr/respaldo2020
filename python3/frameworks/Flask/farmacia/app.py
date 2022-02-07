from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_prueba.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MyConectDB = SQLAlchemy(app)
MyMarshma = Marshmallow(app)


#creo Table Model con Sqlalchemy por facilidad y por muestra de prueba se crean solo string, 
# #pero os pude usar field image float int bool etc
class PrimerTable(MyConectDB.Model):
    id = MyConectDB.Column(MyConectDB.Integer, primary_key=True)
    name = MyConectDB.Column(MyConectDB.String(70), unique=True)
    description = MyConectDB.Column(MyConectDB.String(100))
    precio = MyConectDB.Column(MyConectDB.String(100))
    foto = MyConectDB.Column(MyConectDB.String(100))
    fotob = MyConectDB.Column(MyConectDB.String(100))

    def __init__(self, name, description,precio,foto,fotob ):
        self.name = name
        self.description = description
        self.precio = precio
        self.foto = foto
        self.fotob = fotob
        

#commit en database x
MyConectDB.create_all()
print('se ha creado table')
#creo mi squema
class productochema(MyMarshma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'precio', 'foto', 'fotob')


MySquema = productochema()
MySquemas = productochema(many=True)



@app.route('/producto', methods=['Post'])
def create_product():
  name = request.json['name']
  description = request.json['description']
  precio = request.json['precio']
  foto = request.json['foto']
  fotob = request.json['fotob']

  
  new_product= PrimerTable(name, description,precio,foto,fotob)
  
  MyConectDB.session.add(new_product)
  
  MyConectDB.session.commit()
  print('se ha creado un nuevo producto')
  return MySquema.jsonify(new_product)


@app.route('/producto', methods=['GET'])
def get_producto():
      
  all_producto = PrimerTable.query.all()
  result = MySquemas.dump(all_producto)
  print('aqui los resultado')
  print(result)
  return jsonify(result)

@app.route('/producto/<id>', methods=['GET'])
def get_product(id):
  product = PrimerTable.query.get(id)
  return MySquema.jsonify(product)

@app.route('/producto/<id>', methods=['PUT'])
def update_product(id):
  product = PrimerTable.query.get(id)

  name = request.json['name']
  description = request.json['description']
  precio = request.json['precio']
  foto = request.json['foto']
  fotob = request.json['fotob']

  product.name = name
  product.description = description

  MyConectDB.session.commit()

  return MySquema.jsonify(product)

@app.route('/producto/<id>', methods=['DELETE'])
def delete_product(id):
  product = PrimerTable.query.get(id)
  MyConectDB.session.delete(product)
  MyConectDB.session.commit()
  return MySquema.jsonify(product)


@app.route('/', methods=['GET'])
def index():
    return jsonify(
        {
            'message': 'Welcome to my API',
            'urls': ['/producto/<id>', '/producto' , 'with post get delete update']
            }
        )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8989)

