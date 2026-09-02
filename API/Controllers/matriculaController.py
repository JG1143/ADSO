from flask import jsonify
from Services.matriculaService import matriculaService


class matriculaController:

    def show():
        data = matriculaService.show()
        return jsonify(data), 200