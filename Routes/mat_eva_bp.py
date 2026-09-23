# blueprint  
from flask import Blueprint
from Controllers.mat_eva_Controller import mat_eva_Controller

mateva_bp = Blueprint('mateva_bp', __name__)

@mateva_bp.route('/', methods=['GET'])
def home():
    mat_eva_Controller.show()

@mateva_bp.route('/', methods=['POST'])
def add():
    mat_eva_Controller.add()

@mateva_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    mat_eva_Controller.delete()

@mateva_bp.route('/<uuid>', methods=['PATCH'])
def update():
    mat_eva_Controller.update()