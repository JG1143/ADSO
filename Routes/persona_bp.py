# blueprint  
from flask import Blueprint
from Controllers.PersonaController import PersonaController

per_bp = Blueprint('per_bp', __name__)

@per_bp.route('/', methods=['GET'])
def show():
    return PersonaController.show()

@per_bp.route('/', methods=['POST'])
def add():
    return PersonaController.add()

@per_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    return PersonaController.delete()

@per_bp.route('/<uuid>', methods=['PATCH'])
def update():
    return  PersonaController.update()

@per_bp.route('/<int:id>', methods=['GET'])
def obtener_id():
    return PersonaController.obtener_id()