import sqlite3

def workWithDb(query):
    with sqlite3.connect('database/sanatorium.db') as db:
        cursor = db.cursor()
        cursor.execute(query)


def checkPassword(login, password):
    with sqlite3.connect('database/sanatorium.db') as db:
        cursor = db.cursor()
        for i in cursor.execute(f'SELECT * FROM users'):
            if login == i[0] and password == i[1]:
                return True

