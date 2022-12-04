import datetime
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import script_1
import script_2
import script_3
import script_4
import iterators


class GismeteoApplication(QWidget):

    def __init__(self):
        super().__init__()
        self.application()

    def application(self):
        self.window()
        print(1)
        self.resize(600, 480)
        self.setWindowTitle("Application")

        btn_1 = QPushButton('Создать исходный файл', self)
        btn_1.resize(350, 40)
        # btn_1.clicked.connect()

        btn_2 = QPushButton('Разделить исходный файл по файлам X.csv и Y.csv', self)
        btn_2.move(0, 40)
        btn_2.resize(350, 40)
        # btn_2.clicked.connect()

        btn_3 = QPushButton('Разделить исходный файл по годам', self)
        btn_3.move(0, 80)
        btn_3.resize(350, 40)
        # btn_3.clicked.connect()

        btn_4 = QPushButton('Разделить исходный файл по неделям', self)
        btn_4.move(0, 120)
        btn_4.resize(350, 40)
        # btn_4.clicked.connect()

        btn_5 = QPushButton('Найти данные по дате в файлах X.csv и Y.csv', self)
        btn_5.move(0, 160)
        btn_5.resize(350, 40)
        # btn_5.clicked.connect()

        btn_6 = QPushButton('Найти данные по дате в датасете разбитом по годам', self)
        btn_6.move(0, 200)
        btn_6.resize(350, 40)
        # btn_6.clicked.connect()

        btn_7 = QPushButton('Найти данные по дате в датасете разбитом по неделям', self)
        btn_7.move(0, 240)
        btn_7.resize(350, 40)
        # btn_7.clicked.connect()

        btn_8 = QPushButton('Вызвать итератор датасета разбитого на файлы X.csv и Y.csv', self)
        btn_8.move(0, 280)
        btn_8.resize(350, 40)
        # btn_8.clicked.connect()

        btn_9 = QPushButton('Вызвать итератор датасета разбитого по годам', self)
        btn_9.move(0, 320)
        btn_9.resize(350, 40)
        # btn_9.clicked.connect()

        btn_10 = QPushButton('Вызвать итератор датасета разбитого по неделям', self)
        btn_10.move(0, 360)
        btn_10.resize(350, 40)
        # btn_10.clicked.connect()

        btn_11 = QPushButton('Вызвать итератор исходного датасета', self)
        btn_11.move(0, 400)
        btn_11.resize(350, 40)
        btn_11.clicked.connect(self.start_iter)

        exit_button = QPushButton('Выход', self)
        exit_button.clicked.connect(QCoreApplication.instance().quit)
        exit_button.move(0, 440)
        exit_button.resize(350, 40)

        self.show()

    def start_iter(self):
        _msg = QMessageBox()
        _msg.setWindowTitle('Сообщение')
        _msg.setText('Выберите исходный файл, по которому провести итерацию')
        _msg.exec_()
        file_path = QFileDialog.getOpenFileName(self, 'Select Folder', filter="*.csv")[0]
        obj = iterators.DateIterator(file_path)

        window_1 = QMessageBox()
        window_1.addButton('Начать', QMessageBox.AcceptRole)
        window_1.addButton('Отмена', QMessageBox.RejectRole)
        window_1.setWindowTitle('Итератор')
        window_1.exec()

        while True:

            if window_1.clickedButton().text() == 'Начать':

                window_2 = QMessageBox()
                item = next(obj)
                text = 'Вывод итератора:' + str(item)
                window_2.setWindowTitle('Результат итерации')
                window_2.setText(text)
                window_2.addButton('Продолжить', QMessageBox.AcceptRole)
                window_2.addButton('Прекратить итерацию', QMessageBox.RejectRole)
                window_2.exec()

                if window_2.clickedButton().text() == 'Прекратить итерацию':
                    break

            elif window_1.clickedButton().text() == 'Отмена':
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GismeteoApplication()
    sys.exit(app.exec_())
