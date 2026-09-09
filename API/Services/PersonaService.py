from flask import current_app
from Models.Persona import Persona

class PersonaService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add():
        pass

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_PERSONA"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        print(data)
        return ""
        
    def obtener_id(id):
        sql = "SELECT * FROM T_PERSONA WHERE PER_ID = %s"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql,(id,))
        data = c.fetchone()
        if data is None:
            return "No se encontro la persona "
        id_per = Persona(data[0])
        c.close()
        return id_per