# blueprint  
from flask import Blueprint
from Controllers.InstructorController import InstructorController

inst_bp = Blueprint('inst_bp', __name__)

@inst_bp.route('/', methods=['GET'])
def show():
    return InstructorController.show()

@inst_bp.route('/', methods=['POST'])
def add():
    return InstructorController.add()

@inst_bp.route('/<uuid>', methods=['DELETE'])
def delete():
    return InstructorController.delete()

@inst_bp.route('/<uuid>', methods=['PATCH'])
def update():
    return InstructorController.update()