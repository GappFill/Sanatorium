from cl import proc_window, ui
from manageDB import workWithDb
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem
from messages import Warning

class cl_work():
    def open(self):
        proc_window.show()
        fill()
        fill_combobox()

    def delet_employee(self):  # Функиция удаления сотрудника
        returnValue = Warning()
        if returnValue == True:
            row = ui.table_proc.currentIndex().row()
            workWithDb(f"DELETE FROM cl WHERE Field7='{ui.table_proc.model().index(row, 6).data()}'")
            workWithDb(f"UPDATE rooms SET Field4='{'Свободен'}' WHERE Field1='{ui.table_proc.model().index(row, 5).data()}'")
            fill()
            fill_combobox()


    def add1(self):
        str_ = str(ui.comboBox.currentText())
        workWithDb(f"INSERT INTO cl(Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8) VALUES('{ui.room.text()}','{ui.flour.text()}','{ui.place.text()}','{ui.room_2.text()}','{ui.room_3.text()}','{str_}','{ui.room_5.text()}','{ui.room_6.text()}')")
        text = 'Занят до:'+ui.room_3.text()
        workWithDb(f"UPDATE rooms SET Field4='{text}' WHERE Field1='{str(ui.comboBox.currentText())}'")
        ui.room.setText('')
        ui.flour.setText('')
        ui.place.setText('')
        ui.room_2.setText('')
        ui.room_3.setText('')
        ui.room_5.setText('')
        ui.room_6.setText('')
        fill()
        fill_combobox()

    ui.remove_button.clicked.connect(delet_employee)
    ui.back_button.clicked.connect(lambda : proc_window.close())
    ui.add_button.clicked.connect(add1)

def fill_combobox():
    ui.comboBox.clear()
    with sqlite3.connect('database/sanatorium.db') as db:
        cursor = db.cursor()
        for name in cursor.execute(f"SELECT Field1 FROM rooms WHERE Field4='{'Свободен'}'"):
            ui.comboBox.addItems(list(name))
def fill():
    with sqlite3.connect('database/sanatorium.db') as db:
        cursor = db.cursor()
        ui.table_proc.setRowCount(0)
        for surname_name, name, second_name, GPA, phone_number, email, faculty, ID in cursor.execute(f"SELECT Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8 FROM cl"):
            row = ui.table_proc.rowCount()
            ui.table_proc.setRowCount(row + 1)
            ui.table_proc.setItem(row, 0, QTableWidgetItem(str(surname_name)))
            ui.table_proc.setItem(row, 1, QTableWidgetItem(str(name)))
            ui.table_proc.setItem(row, 2, QTableWidgetItem(str(second_name)))
            ui.table_proc.setItem(row, 3, QTableWidgetItem(str(GPA)))
            ui.table_proc.setItem(row, 5, QTableWidgetItem(str(email)))
            ui.table_proc.setItem(row, 4, QTableWidgetItem(str(phone_number)))
            ui.table_proc.setItem(row, 6, QTableWidgetItem(str(faculty)))
            ui.table_proc.setItem(row, 7, QTableWidgetItem(str(ID)))
        db.commit()

# import sys
# app = QtWidgets.QApplication(sys.argv)
# proc_window = QtWidgets.QWidget()
# ui = Ui_proc_window()
# ui.setupUi(proc_window)

# f"'{ui.room.text()}',"
#                    f"'{ui.flour.text()}',"
#                    f"'{ui.place.text()}',"
#                    f"'{ui.room_2.text()}',"
#                    f"'{ui.room_3.text()}',"
#                    f"'{str_}',"
#                    f"'{ui.room_5.text()}',"
#                    f"'{ui.room_6.text()}'"