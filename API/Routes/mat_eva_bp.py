# blueprint  
from flask import Blueprint
from Controllers.mat_eva_Controller import mat_evaController

mat_eva_bp = Blueprint('mat_eva_bp', __name__)

@mat_eva_bp.route('/', methods=['GET'])
def home():
    mat_evaController.show()

@mat_eva_bp.route('/', methods=['POST'])
def add():
    return "agregar resultado de matricula y evaluacion"