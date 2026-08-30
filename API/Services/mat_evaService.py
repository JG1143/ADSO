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
        print(data)
        # c.close()
        return ""
