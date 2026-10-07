# blueprint  
from flask import Blueprint
from Controllers.imparteController import imparteController

imp_bp = Blueprint('imp_bp', __name__)

@imp_bp.route('/', methods=['GET'])
def show():
    return imparteController.show()

@imp_bp.route('/', methods=['POST'])
def add():
    return imparteController.add()

@imp_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    return imparteController.delete()

@imp_bp.route('/<uuid>', methods=['PATCH'])
def update():
    return imparteController.update()