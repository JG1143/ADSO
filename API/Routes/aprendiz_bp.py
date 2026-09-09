# blueprint  
from flask import Blueprint
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def home():
    aprendizController.show()

@apr_bp.route('/', methods=['POST'])
def add():
    aprendizController.add()

@apr_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    aprendizController.delete()

@apr_bp.route('/', methods=['POST'])
def update():
    aprendizController.update()