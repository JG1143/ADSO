from flask import jsonify,request
from Services.matriculaService import matriculaService


class matriculaController:

    def show():
        data = matriculaService.show()
        return jsonify(data), 200

    def add(data):
                data = request.get_json(silent=True)
                if data is None :
                    return jsonify({"mensaje": "json invalido"}), 400
                campo_req = ("estado","fecha_inscripcion","apr_id","cur_id")
                faltantes = [W for W in campo_req if W not in data]
        
                if len(faltantes) > 0 :
                    return jsonify({"mensaje":f"faltan parametros {faltantes}"}), 400

                if  data.get("estado") is str:
                    return jsonify({"mensaje": "el estado debe ser cadena de texto"}), 400


                if data.get("fecha_inscripcion") is not "yyyy/mm/dd":
                            return jsonify({"mensaje": "el formato debe ser yyyy/mm/dd"}),400
                elif  data.get("fecha_inscripcion") is not str :
                            return jsonify({"mensaje": "el formato debe ser yyyy/mm/dd"}),400


                if  data.get("apr_id") is int:
                    return jsonify({"mensaje": "el apr_id debe ser numero entero"}), 400


                if  data.get("cur_id") is int:
                    return jsonify({"mensaje": "el cur_id debe ser numero entero"}), 400




                x = matriculaService.add(data)
                return jsonify(x),201
                                
                                
                                
    def delete(uuid):
        x = matriculaService.delete(uuid)
        if x == 200:
            jsonify ({"mensaje": f"se elimino la matricula con el uuid:{uuid}"}),200
        else:
            return jsonify({"mensaje": f"no se encontro la matricula con el uuid{uuid}"}),404





    def update(uuid):
            data = request.get_json()
            campos_req = ['estado', 'fecha_inscripcion', 'apr_id', 'cur_id']
            faltantes = [w for w in campos_req if w not in data]
    
            if len(faltantes) > 0:
                return jsonify({"faltan campos": faltantes}), 400
    
            x = matriculaService.update(uuid, data)
            if x == 200:
                return jsonify({"mensaje": f"se actualizo la matricula con uuid: {uuid}"}), 200
            else:
                return jsonify({"mensaje": f"no se encontro la matricula con uuid: {uuid}"}), 404



                