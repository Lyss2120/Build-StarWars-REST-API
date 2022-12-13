"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Vehicles
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():
    # all_people = User.query.all()
    # print(all_people[0].__repr__())
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods= ['GET'])
def get_people():
    return jsonify({
        "mensaje": "todos los personajes",
        "people": []
    })

@app.route('/planets', methods= ['GET'])
def get_planets():
    return jsonify({
        "mensaje": "todos los planetas",
        "planets": []
    })

@app.route('/vehicles', methods= ['GET'])
def get_vehicles():
    return jsonify({
        "mensaje": "todos los vehiculos",
        "vehicles": []
    })

@app.route('/people/<int:people_id>', methods= ['GET'])
def get_people():
    return jsonify({
        "aqui ira la funcion para traer un personaje segun su posision": "get an element from a list by position"
    })

@app.route('/planets/<int:planets_id>', methods= ['GET'])
def get_planets():
    return jsonify({
        "aqui ira la funcion para traer un planeta segun su posision": "get an element from a list by position"
    })








# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
