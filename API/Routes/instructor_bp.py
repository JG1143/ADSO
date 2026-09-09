# blueprint  
from flask import Blueprint
from Controllers.InstructorController import InstructorController

inst_bp = Blueprint('inst_bp', __name__)

@inst_bp.route('/', methods=['GET'])
def home():
    InstructorController.show()

@inst_bp.route('/', methods=['POST'])
def add():
    InstructorController.add()

@inst_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    InstructorController.delete()

@inst_bp.route('/', methods=['POST'])
def update():
    InstructorController.update()