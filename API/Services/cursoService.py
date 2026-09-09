from flask import current_app
from Models.curso import curso
import uuid
class cursoService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
        uuid_cur = uuid.uuid4()
        c  = current_app.mysql.connection.cursor()
        sql = """ INSERT INTO T_CURSO(CUR_UUID,CUR_NOMBRE,CUR_DESCRIPCION,CUR_DURACION,CUR_FECHA_INICIO,CUR_FECHA_FIN) 
                    VALUES (%s,%s,%s,%s,%s,%s)"""
        c.execute(sql,(uuid_cur,data["nombre"],data["descripcion"],data["duracion"],data["fecha_inicio"],data["fecha_fin"]))
        c.connection.commit()
        id = c.lastrowid
        c.close()
        respuesta = {"id": id,"uuid": uuid_cur,
                        "nombre":data["nombre"],
                        "descripcion":data["descripcion"],
                        "duracion":data["duracion"],
                        "fecha_inicio":data["fecha_inicio"],
                        "fecha_fin":data["fecha_fin"]}
        return respuesta

        pass

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_CURSO"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [curso(x[0], x[1], x[2], x[3], x[4], x[5], x[6]) for x in data]
        c.close()
        return data
