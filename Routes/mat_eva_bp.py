# blueprint  
from flask import Blueprint
from Controllers.mat_eva_Controller import mat_evaController

mateva_bp = Blueprint('mateva_bp', __name__)

@mateva_bp.route('/', methods=['GET'])
def show():
    return mat_evaController.show()

@mateva_bp.route('/', methods=['POST'])
def add():
    return mat_evaController.add()

@mateva_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    return mat_evaController.delete()

@mateva_bp.route('/<uuid>', methods=['PATCH'])
def update():
    return mat_evaController.update()