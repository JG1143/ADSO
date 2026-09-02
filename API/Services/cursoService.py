from flask import current_app
from Models.curso import curso

class cursoService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add():
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
