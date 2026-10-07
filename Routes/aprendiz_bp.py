# blueprint  
from flask import Blueprint
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def show():
    return aprendizController.show()


@apr_bp.route('/', methods=['POST'])
def add():
     return aprendizController.add()

@apr_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    return aprendizController.delete()

@apr_bp.route('/<uuid>', methods=['PATCH'])
def update():
    return aprendizController.update()