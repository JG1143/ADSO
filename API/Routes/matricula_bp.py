# blueprint  
from flask import Blueprint
from Controllers.matriculaController import matriculaController

mat_bp = Blueprint('mat_bp', __name__)

@mat_bp.route('/', methods=['GET'])
def home():
    matriculaController.show()

@mat_bp.route('/', methods=['POST'])
def add():
    return "agregar matricula"