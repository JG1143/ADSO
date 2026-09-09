# blueprint  
from flask import Blueprint
from Controllers.mat_eva_Controller import mat_evaController

mat_eva_bp = Blueprint('mat_eva_bp', __name__)

@mat_eva_bp.route('/', methods=['GET'])
def home():
    mat_eva_Controller.show()

@mat_eva_bp.route('/', methods=['POST'])
def add():
    mat_eva_Controller.add()

@mat_eva_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    mat_eva_Controller.delete()

@mat_eva_bp.route('/', methods=['POST'])
def update():
    mat_eva_Controller.update()