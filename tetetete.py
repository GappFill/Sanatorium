import sqlite3

mas = []
with sqlite3.connect('database/sanatorium.db') as db:
    cursor = db.cursor()
    for i in cursor.execute(f"""SELECT Field1,Field2,Field3,Field4 FROM empl"""):
        new_i = i[0] + ' ' + i[1][0] + '.' + i[2][0] + '. - ' + i[3]
        mas.append(new_i)
print(mas)
