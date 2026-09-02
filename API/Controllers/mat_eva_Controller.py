from flask import jsonify
from Services.mat_evaService import mat_evaService


class mat_evaController:

    def show():
        data = mat_evaService.show()
        return jsonify(data), 200