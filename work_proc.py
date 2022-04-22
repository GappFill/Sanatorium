from proc import proc_window, ui
from manageDB import workWithDb
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from messages import Warning

class proc_work():
    def add(self):
         workWithDb(f"INSERT INTO proc(Field1,Field2,Field3,Field4,Field5,Field6) VALUES("
                    f"'{ui.name.text()}',"
                    f"'{ui.room.text()}',"
                    f"'{ui.time.text()}',"
                    f"'{ui.rest.text()}',"
                    f"'{ui.more.currentText()}',"
                    f"NULL)")
         ui.name.setText('')
         ui.room.setText('')
         ui.time.setText('')
         ui.rest.setText('')
         fill()

    def open(self):
        proc_window.show()
        fill()
        fillCombo()

    def delet_employee(self):  # Функиция удаления сотрудника
        returnValue = Warning()
        if returnValue == True:
            row = ui.table_proc.currentIndex().row()
            workWithDb(f"DELETE FROM proc WHERE Field6={ui.table_proc.model().index(row, 5).data()}")
            fill()

    def search(self):
        name = ui.search_entry.text()
        if name == '':
            fill()
        with sqlite3.connect('database/sanatorium.db') as db:
            cursor = db.cursor()
            ui.table_proc.setRowCount(0)
            for surname, name, second_name, salary, phone, adress in cursor.execute(
                    f"SELECT * FROM proc WHERE Field1 LIKE '%'||?||'%' OR Field2 LIKE '%'||?||'%' OR Field3 LIKE '%'||?||'%' OR Field4 LIKE '%'||?||'%' OR Field5 LIKE '%'||?||'%' OR Field6 LIKE '%'||?||'%'",
                    (name, name, name, name, name, name)):
                row = ui.table_proc.rowCount()
                ui.table_proc.setRowCount(row + 1)
                ui.table_proc.setItem(row, 0, QTableWidgetItem(str(surname)))
                ui.table_proc.setItem(row, 1, QTableWidgetItem(str(name)))
                ui.table_proc.setItem(row, 2, QTableWidgetItem(str(second_name)))
                ui.table_proc.setItem(row, 3, QTableWidgetItem(str(salary)))
                ui.table_proc.setItem(row, 4, QTableWidgetItem(str(phone)))
                ui.table_proc.setItem(row, 5, QTableWidgetItem(str(adress)))
            db.commit()

    close = ui.back_button.clicked.connect(lambda: proc_window.close())
    add = ui.add_button.clicked.connect(add)
    delet = ui.remove_button.clicked.connect(delet_employee)
    search = ui.search_button.clicked.connect(search)
    ui.table_proc.setColumnHidden(5, True)

def fillCombo():
    mas = []
    with sqlite3.connect('database/sanatorium.db') as db:
        cursor = db.cursor()
        for i in cursor.execute(f"""SELECT Field1,Field2,Field3,Field4 FROM empl"""):
            new_i = i[0] + ' ' + i[1][0] + '.' + i[2][0] + '. - ' + i[3]
            mas.append(new_i)
    ui.more.clear()
    ui.more.addItems(mas)

def fill():
    with sqlite3.connect('database/sanatorium.db') as db:
        cursor = db.cursor()
        ui.table_proc.setRowCount(0)
        for surname_name, name, second_name, GPA, phone_number, email in cursor.execute(f"SELECT Field1,Field2,Field3,Field4,Field5,Field6 FROM proc"):
            row = ui.table_proc.rowCount()
            ui.table_proc.setRowCount(row + 1)
            ui.table_proc.setItem(row, 0, QTableWidgetItem(str(surname_name)))
            ui.table_proc.setItem(row, 1, QTableWidgetItem(str(name)))
            ui.table_proc.setItem(row, 2, QTableWidgetItem(str(second_name)))
            ui.table_proc.setItem(row, 3, QTableWidgetItem(str(GPA)))
            ui.table_proc.setItem(row, 4, QTableWidgetItem(str(phone_number)))
            ui.table_proc.setItem(row, 5, QTableWidgetItem(str(email)))
        db.commit()