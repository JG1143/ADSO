from flask import jsonify,request
from Services.cursoService import cursoService



class cursoController:

    def show():
        data = cursoService.show()
        return jsonify(data), 200


    def add(data):
            data = request.get_json(silent=True)
            if data is None :
                return jsonify({"mensaje": "json invalido"}), 400
            campo_req = ("nombre","codigo","duracion","costo","descripcion")
            faltantes = [W for W in campo_req if W not in data]

            if len(faltantes) > 0 :
                return jsonify({"mensaje":f"faltan parametros {faltantes}"}), 400

            if data.get("nombre") is not str:
                return jsonify ({"mensaje": "el nombre debe ser una cadena de texto"}), 400

            if data.get("codigo") is not int:
                return jsonify({"mensaje": "el codigo del curso debe ser un numero entero "}), 400

            
            if data.get("duracion") is not int:
                return jsonify({"mensaje": "la duracion  debe ser un numero entero "}), 400


            if data.get("costo") is not int:
                return jsonify({"mensaje": "el costo debe ser un numero entero"}), 400

            
            if data.get("descripcion") is not str:
                return jsonify({"mensaje": "la descripcion debe ser una cadena de texto"}), 400
            
             
            x = cursoService.add(data)
            return jsonify(x),201



    def delete(uuid):
        x = cursoService.delete(uuid)
        if x == 200:
            return jsonify ({"mensaje": f"se elimino el curso con uuid :{uuid}"}), 200
        else:
            return jsonify ({"mensaje": f"curso no encontrado con el uuid :{uuid}"}), 404




    def update(uuid):
        data = request.get_json()
        campos_req = ['nombre', 'codigo', 'duracion', 'costo', 'descripcion']
        faltantes = [w for w in campos_req if w not in data]
        
        if len(faltantes) > 0:
            return jsonify({"faltan campos": faltantes}), 400
         
      
        
        x = cursoService.update(uuid, data)
        if x == 200:
                return jsonify({"mensaje": f"se actualizo el curso con uuid: {uuid}"}), 200
        else:
                return jsonify({"mensaje": f"no se encontro el curso con uuid: {uuid}"}), 404