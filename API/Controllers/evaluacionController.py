from flask import jsonify
from Services.evaluacionService import evaluacionService


class evaluacionController:

    def show():
        data = evaluacionService.show()
        return jsonify(data), 200