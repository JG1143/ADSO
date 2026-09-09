
from flask import Blueprint
from Controllers.cursoController import cursoController

cur_bp = Blueprint('cur_bp', __name__)

@cur_bp.route('/', methods=['GET'])
def home():
    cursoController.show()

@cur_bp.route('/', methods=['POST'])
def add():
    cursoController.add()

@cur_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    cursoController.delete()

@cur_bp.route('/', methods=['POST'])
def update():
    cursoController.update()