from flask import jsonify, request
from Services.imparteService import imparteService


class imparteController:

    def show():
        data = imparteService.show()
        return jsonify(data), 200

    def add(data):
            data = request.get_json(silent=True)
            if data is None :
                return jsonify({"mensaje": "json invalido"}), 400
            campo_req = ("rol","fecha_asignacion","cur_id","ins_id")
            faltantes = [W for W in campo_req if W not in data]
    
            if len(faltantes) > 0 :
                return jsonify({"mensaje":f"faltan parametros {faltantes}"}), 400


            if data.get("rol") is not str:
                return jsonify ({"mensaje": "el rol debe ser cadena de texto"}),400

            if data.get("fecha_asignacion") is not "yyyy/mm/dd":
                            return jsonify({"mensaje": "el formato debe ser yyyy/mm/dd"}),400
            elif  data.get("fecha_asignacion") is not str :
                            return jsonify({"mensaje": "el formato debe ser yyyy/mm/dd"}),400

            if data.get("cur_id") is not int: 
                   return jsonify({"mensaje":"el cur_id debe se numero entero"}),400


            if data.get("ins_id") is not int:
                return jsonify({"mensaje": "la ins_id debe ser un numero entero"}), 400



            x = imparteService.add(data)
            return jsonify(x),201



    def delete(uuid):
        x = imparteService.delete(uuid)
        if x == 200:
             jsonify ({"mensaje": f"se elimino imparte con el uuid:{uuid}"}),200
        else:
            return jsonify({"mensaje": f"no se encontro el imparte con el uuid{uuid}"}),404


    def update(uuid):
        data = request.get_json()
        campos_req = ['rol', 'fecha_asignacion', 'cur_id', 'ins_id']
        faltantes = [w for w in campos_req if w not in data]

        if len(faltantes) > 0:
            return jsonify({"faltan campos": faltantes}), 400

        x = imparteService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo el imparte con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el imparte con uuid: {uuid}"}), 404