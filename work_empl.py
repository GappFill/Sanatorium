from empl import emloyee_window, ui
from manageDB import workWithDb
from messages import Warning
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem

class emplFunck():

    def win_show(self):
        emloyee_window.show()
        fill()

    def back(self):
        emloyee_window.close()

    def add(self):
        workWithDb(f"INSERT INTO empl(Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9) VALUES("
                   f"'{ui.surname_entry.text()}',"
                   f"'{ui.name_entry.text()}',"
                   f"'{ui.second_name_entry.text()}',"
                   f"'{ui.post_entry.text()}',"
                   f"'{ui.salary_entry.text()}',"
                   f"'{ui.time_entry.text()}',"
                   f"'{ui.phonenumber_entry.text()}',"
                   f"'{ui.adress_entry.text()}',"
                   f"NULL)")
        ui.surname_entry.setText('')
        ui.name_entry.setText('')
        ui.second_name_entry.setText('')
        ui.post_entry.setText('')
        ui.salary_entry.setText('')
        ui.time_entry.setText('')
        ui.phonenumber_entry.setText('')
        ui.adress_entry.setText('')
        fill()

    def delet_employee(self):  # Функиция удаления сотрудника
        returnValue = Warning()
        if returnValue == True:
            row = ui.employee_window.currentIndex().row()
            workWithDb(f"DELETE FROM empl WHERE Field9={ui.employee_window.model().index(row, 8).data()}")
            fill()

    def search(self):
        name = ui.search_entry.text()
        if name == '':
            fill()
        with sqlite3.connect('database/sanatorium.db') as db:
            cursor = db.cursor()
            ui.employee_window.setRowCount(0)
            for surname, name, second_name, salary, phone, adress, email, f, g in cursor.execute(
                    f"SELECT * FROM empl WHERE Field1 LIKE '%'||?||'%' OR Field2 LIKE '%'||?||'%' OR Field3 LIKE '%'||?||'%' OR Field4 LIKE '%'||?||'%' OR Field5 LIKE '%'||?||'%' OR Field6 LIKE '%'||?||'%' OR Field7 LIKE '%'||?||'%' OR Field8 LIKE '%'||?||'%' OR Field9 LIKE '%'||?||'%'",
                    (name, name, name, name, name, name, name, name, name)):
                row = ui.employee_window.rowCount()
                ui.employee_window.setRowCount(row + 1)
                ui.employee_window.setItem(row, 0, QTableWidgetItem(str(surname)))
                ui.employee_window.setItem(row, 1, QTableWidgetItem(str(name)))
                ui.employee_window.setItem(row, 2, QTableWidgetItem(str(second_name)))
                ui.employee_window.setItem(row, 3, QTableWidgetItem(str(salary)))
                ui.employee_window.setItem(row, 4, QTableWidgetItem(str(phone)))
                ui.employee_window.setItem(row, 5, QTableWidgetItem(str(adress)))
                ui.employee_window.setItem(row, 6, QTableWidgetItem(str(email)))
                ui.employee_window.setItem(row, 7, QTableWidgetItem(str(f)))
                ui.employee_window.setItem(row, 8, QTableWidgetItem(str(g)))
            db.commit()
    back_b = ui.back_button.clicked.connect(back)
    add_b = ui.add_button.clicked.connect(add)
    delet = ui.remove_button.clicked.connect(delet_employee)
    search = ui.search_button.clicked.connect(search)
    ui.employee_window.setColumnHidden(8, True)

def fill():
    with sqlite3.connect('database/sanatorium.db') as db:
        cursor = db.cursor()
        ui.employee_window.setRowCount(0)
        for surname_name, name, second_name, GPA, phone_number, email, faculty, ID, kk in cursor.execute(f"SELECT Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9 FROM empl"):
            row = ui.employee_window.rowCount()
            ui.employee_window.setRowCount(row + 1)
            ui.employee_window.setItem(row, 0, QTableWidgetItem(str(surname_name)))
            ui.employee_window.setItem(row, 1, QTableWidgetItem(str(name)))
            ui.employee_window.setItem(row, 2, QTableWidgetItem(str(second_name)))
            ui.employee_window.setItem(row, 3, QTableWidgetItem(str(GPA)))
            ui.employee_window.setItem(row, 4, QTableWidgetItem(str(phone_number)))
            ui.employee_window.setItem(row, 5, QTableWidgetItem(str(email)))
            ui.employee_window.setItem(row, 6, QTableWidgetItem(str(faculty)))
            ui.employee_window.setItem(row, 7, QTableWidgetItem(str(ID)))
            ui.employee_window.setItem(row, 8, QTableWidgetItem(str(kk)))
        db.commit()

