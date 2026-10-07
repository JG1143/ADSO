# blueprint  
from flask import Blueprint
from Controllers.evaluacionController import evaluacionController

eva_bp = Blueprint('eva_bp', __name__)

@eva_bp.route('/', methods=['GET'])
def show():
    return evaluacionController.show()

@eva_bp.route('/', methods=['POST'])
def add():
    return evaluacionController.add()

@eva_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    return evaluacionController.delete()

@eva_bp.route('/<uuid>', methods=['PATCH'])
def update():
    return evaluacionController.update()