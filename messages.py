from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox


def Error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Ошибка")
    msg.setInformativeText('Введены неккоректные данные! Попробуйте еще раз!')
    msg.setWindowTitle("Ошибка соотвествия")
    msg.exec_()

def Warning():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText("Вы точно хотите выполнить удаление?")
    msg.setWindowTitle("Подтверждение операции")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

    returnValue = msg.exec()
    if returnValue == QMessageBox.Yes:
        return True