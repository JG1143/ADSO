
from flask import Blueprint
from Controllers.cursoController import cursoController

cur_bp = Blueprint('cur_bp', __name__)

@cur_bp.route('/', methods=['GET'])
def home():
    cursoController.show()

@cur_bp.route('/', methods=['POST'])
def add():
    return "agregar curso"