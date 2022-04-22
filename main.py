from manageDB import workWithDb, checkPassword
from auth import Ui_auth_window
from reg import Ui_reg_window
from mwindow import Ui_main_window
from messages import Error
from work_empl import emplFunck
from work_proc import proc_work
from work_room import rooms_work
from worck_cl import cl_work


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)

#Окно авторизации
auth_window = QtWidgets.QWidget()
ui_auth = Ui_auth_window()
ui_auth.setupUi(auth_window)
auth_window.show()

#Окно регистрации
reg_window = QtWidgets.QWidget()
ui_reg = Ui_reg_window()
ui_reg.setupUi(reg_window)

#Основное окно
main_window = QtWidgets.QWidget()
ui_main = Ui_main_window()
ui_main.setupUi(main_window)


def check():
    if checkPassword(ui_auth.loginEntry.text(), ui_auth.pswEntry.text()) == True:
        auth_window.close()
        main_window.show()
    else:
        Error()



def reg():
    workWithDb(f"INSERT INTO users VALUES('{ui_reg.login_entry.text()}', '{ui_reg.psw_entry.text()}', NULL)")
    reg_window.close()


ui_auth.auth_entry_button.clicked.connect(check)
ui_auth.auth_reg_button.clicked.connect(lambda : reg_window.show())
ui_reg.reg_button.clicked.connect(reg)
ui_reg.back_button.clicked.connect(lambda : reg_window.close())

#Создать кнопки,базы данных
ui_main.rooms_button_2.clicked.connect(lambda : main_window.close())#Кнопка закрытия основного окна
#Кнопки окна сотрудников
ui_main.employee_button.clicked.connect(emplFunck.win_show)
# emplFunck.back_b
# emplFunck.add_b
# emplFunck.delet

#Кнопки окна процедур
ui_main.procedures_button.clicked.connect(proc_work.open)
# proc_work.close
# proc_work.add
# proc_work.delet

ui_main.rooms_button.clicked.connect(rooms_work.open)
ui_main.clients_button.clicked.connect(cl_work.open)

sys.exit(app.exec_())