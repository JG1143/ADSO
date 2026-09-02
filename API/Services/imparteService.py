from flask import current_app
from Models.imparte import imparte

class imparteService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add():
        pass

    def delete():
        pass

    def update():
        pass

    def show():
        sql = "SELECT * FROM T_IMPARTE"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [imparte(x[0], x[1], x[2], x[3], x[4], x[5]) for x in data]
        c.close()
        return data
