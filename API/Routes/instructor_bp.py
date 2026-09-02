# blueprint  
from flask import Blueprint
from Controllers.InstructorController import InstructorController

inst_bp = Blueprint('inst_bp', __name__)

@inst_bp.route('/', methods=['GET'])
def home():
    InstructorController.show()

@inst_bp.route('/', methods=['POST'])
def add():
    return "agregar instructor"