from flask import current_app
from Models.mat_eva import mat_eva

class mat_evaService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add():
        pass

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_MAT_EVA"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [mat_eva(x[0], x[1], x[2], x[3], x[4]) for x in data]
        c.close()
        return data
