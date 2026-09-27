# blueprint  
from flask import Blueprint
from Controllers.mat_eva_Controller import mat_evaController

mateva_bp = Blueprint('mateva_bp', __name__)

@mateva_bp.route('/', methods=['GET'])
def home():
    mat_evaController.show()

@mateva_bp.route('/', methods=['POST'])
def add():
    mat_evaController.add()

@mateva_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    mat_evaController.delete()

@mateva_bp.route('/<uuid>', methods=['PATCH'])
def update():
    mat_evaController.update()