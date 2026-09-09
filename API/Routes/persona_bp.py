# blueprint  
from flask import Blueprint
from Controllers.PersonaController import PersonaController

per_bp = Blueprint('per_bp', __name__)

@per_bp.route('/', methods=['GET'])
def home():
    PersonaController.show()

@per_bp.route('/', methods=['POST'])
def add():
    PersonaController.add()

@per_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    PersonaController.delete()

@per_bp.route('/', methods=['POST'])
def update():
    PersonaController.update()

@per_bp.route('/<int:id>', methods=['get'])
def obtener_id():
    PersonaController.obtener_id()