from flask import jsonify,request
from Services.cursoService import cursoService


class cursoController:

    def show():
        data = cursoService.show()
        return jsonify(data), 200


    def add():
            data = request.get_json(silent=True)
            if data is None :
                return jsonify({"mensaje": "json invalido"}), 400
            campo_req = ("nombre","codigo","duracion","costo","descripcion")
            faltantes = [W for W in campo_req if W not in data]

            
            if len(faltantes) > 0 :
                return jsonify({"mensaje":f"faltan parametros {faltantes}"}), 400

            try:
               if type(data.get("nombre")) != str:
                   raise TypeError
            except TypeError:
                    return jsonify({"mensaje":"El nombre debe enviarse como cadena de texto"}), 400
                
            try:
                if type(data.get("codigo")) != int:
                    raise TypeError
            
            except TypeError:
                return jsonify({
                    "mensaje": "El código debe enviarse como un número entero"
                }), 400

            try:
                if type(data.get("duracion")) != int:
                    raise TypeError
            except TypeError:
                return jsonify({ "mensaje" : " La duracion debe enviarse como un numero entero"}), 400


            try: 
                if type(data.get("costo")) not in (int,float) :
                    raise TypeError
            except TypeError:
                return jsonify({"mensaje": " El costo debe enviarse como un numero decimal "}), 400
        
            try:
               if type(data.get("descripcion")) != str:
                   raise TypeError
            except TypeError:
               return jsonify({"mensaje":"La descripcion debe enviarse como cadena de texto"}), 400
            
             
            x = cursoService.add(data)
            return jsonify(x),201



    def delete(uuid):
        x = cursoService.delete(uuid)
        if x == 200:
            return jsonify ({"mensaje": f"se elimino el curso con uuid :{uuid}"}), 200
        else:
            return jsonify ({"mensaje": f"curso no encontrado con el uuid :{uuid}"}), 404




    def update(uuid):
        data = request.get_json(silent=True)
        
        if not isinstance(data,dict):
            return jsonify({"mensaje": "JSON invalido"}), 400

        campos_req = ['nombre', 'codigo', 'duracion', 'costo', 'descripcion']
        faltantes = [w for w in campos_req if w not in data]
        
        if len(faltantes) > 0:
            return jsonify({"faltan campos": faltantes}), 400
         
      
        
        x = cursoService.update(uuid, data)
        if x == 200:
                return jsonify({"mensaje": f"se actualizo el curso con uuid: {uuid}"}), 200
        else:
                return jsonify({"mensaje": f"no se encontro el curso con uuid: {uuid}"}), 404
