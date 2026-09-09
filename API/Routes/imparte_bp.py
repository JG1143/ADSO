# blueprint  
from flask import Blueprint
from Controllers.imparteController import imparteController

imp_bp = Blueprint('imp_bp', __name__)

@imp_bp.route('/', methods=['GET'])
def home():
    imparteController.show()

@imp_bp.route('/', methods=['POST'])
def add():
    imparteController.add()

@imp_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    imparteController.delete()

@imp_bp.route('/', methods=['POST'])
def update():
    imparteController.update()