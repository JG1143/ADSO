from flask import jsonify
from Services.imparteService import imparteService


class imparteController:

    def show():
        data = imparteService.show()
        return jsonify(data), 200