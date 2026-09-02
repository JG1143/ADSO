from flask import jsonify
from Services.InstructorService import InstructorService


class InstructorController:

    def show():
        data = InstructorService.show()
        return jsonify(data), 200


