import datetime
import os
import sys
import pandas as pd

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
        self.resize(600, 440)
        self.setWindowTitle("Application")

        btn_2 = QPushButton('Разделить исходный файл по файлам X.csv и Y.csv', self)
        btn_2.resize(350, 40)
        btn_2.clicked.connect(self.start_create_x_y)

        btn_3 = QPushButton('Разделить исходный файл по годам', self)
        btn_3.move(0, 40)
        btn_3.resize(350, 40)
        btn_3.clicked.connect(self.start_create_year)

        btn_4 = QPushButton('Разделить исходный файл по неделям', self)
        btn_4.move(0, 80)
        btn_4.resize(350, 40)
        btn_4.clicked.connect(self.start_create_week)

        btn_5 = QPushButton('Найти данные по дате в файлах X.csv и Y.csv', self)
        btn_5.move(0, 120)
        btn_5.resize(350, 40)
        # btn_5.clicked.connect()

        btn_6 = QPushButton('Найти данные по дате в датасете разбитом по годам', self)
        btn_6.move(0, 160)
        btn_6.resize(350, 40)
        # btn_6.clicked.connect()

        btn_7 = QPushButton('Найти данные по дате в датасете разбитом по неделям', self)
        btn_7.move(0, 200)
        btn_7.resize(350, 40)
        # btn_7.clicked.connect()

        btn_8 = QPushButton('Вызвать итератор датасета разбитого на файлы X.csv и Y.csv', self)
        btn_8.move(0, 240)
        btn_8.resize(350, 40)
        btn_8.clicked.connect(self.start_iter_xy)

        btn_9 = QPushButton('Вызвать итератор датасета разбитого по годам', self)
        btn_9.move(0, 280)
        btn_9.resize(350, 40)
        btn_9.clicked.connect(self.start_iter_year)

        btn_10 = QPushButton('Вызвать итератор датасета разбитого по неделям', self)
        btn_10.move(0, 320)
        btn_10.resize(350, 40)
        btn_10.clicked.connect(self.start_iter_week)

        btn_11 = QPushButton('Вызвать итератор исходного датасета', self)
        btn_11.move(0, 360)
        btn_11.resize(350, 40)
        btn_11.clicked.connect(self.start_iter)

        exit_button = QPushButton('Выход', self)
        exit_button.clicked.connect(QCoreApplication.instance().quit)
        exit_button.move(0, 400)
        exit_button.resize(350, 40)

        self.show()

    def start_create_week(self):
        i = 1
        while i < 2:
            _msg = QMessageBox()
            _msg.setWindowTitle('Сообщение')
            _msg.setText('Выберите исходный файл, затем директорию куда сохранить вывод')
            _msg.exec_()

            file_path = QFileDialog.getOpenFileName(self, "Напишите название файла", filter="*.csv")[0]
            output_directory = QFileDialog.getExistingDirectory(self, 'Select Folder')

            if not os.path.exists(file_path):
                break
            if not os.path.exists(output_directory):
                break

            script_3.main_2(file_path, output_directory)
            done_msg = QMessageBox()
            done_msg.setWindowTitle('Сообщение')
            done_msg.setText('Файлы созданы по адресу :' + str(os.path.join(output_directory)))
            done_msg.exec_()
            i = i + 1

    def start_create_year(self):
        i = 1
        while i < 2:
            _msg = QMessageBox()
            _msg.setWindowTitle('Сообщение')
            _msg.setText('Выберите исходный файл, затем директорию куда сохранить вывод')
            _msg.exec_()

            file_path = QFileDialog.getOpenFileName(self, "Напишите название файла", filter="*.csv")[0]
            output_directory = QFileDialog.getExistingDirectory(self, 'Select Folder')

            if not os.path.exists(file_path):
                break
            if not os.path.exists(output_directory):
                break

            script_2.main_2(file_path, output_directory)
            done_msg = QMessageBox()
            done_msg.setWindowTitle('Сообщение')
            done_msg.setText('Файлы созданы по адресу :' + str(os.path.join(output_directory)))
            done_msg.exec_()
            i = i + 1

    def start_create_x_y(self):
        i = 1
        while i < 2:
            _msg = QMessageBox()
            _msg.setWindowTitle('Сообщение')
            _msg.setText('Выберите исходный файл, затем директорию куда сохранить вывод')
            _msg.exec_()

            file_path = QFileDialog.getOpenFileName(self, "Напишите название файла", filter="*.csv")[0]
            output_directory = QFileDialog.getExistingDirectory(self, 'Select Folder')

            if not os.path.exists(file_path):
                break
            if not os.path.exists(output_directory):
                break

            script_1.create_x_y(file_path, output_directory)

            done_msg = QMessageBox()
            done_msg.setWindowTitle('Сообщение')
            done_msg.setText('Файлы созданы по адресу :' + str(os.path.join(output_directory)))
            done_msg.exec_()
            i = i + 1

    def start_iter(self):
        i = 1
        while i < 2:
            _msg = QMessageBox()
            _msg.setWindowTitle('Сообщение')
            _msg.setText('Выберите исходный файл, по которому провести итерацию')
            _msg.exec_()
            file_path = QFileDialog.getOpenFileName(self, 'Select Folder', filter="*.csv")[0]
            if not os.path.exists(file_path):
                break
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
            i = i + 1

    def start_iter_xy(self):
        i = 1
        while i < 2:
            _msg = QMessageBox()
            _msg.setWindowTitle('Сообщение')
            _msg.setText('Выберите файл X')
            _msg.exec_()
            file_path_1 = QFileDialog.getOpenFileName(self, 'Select Folder', filter="*.csv")[0]
            if not os.path.exists(file_path_1):
                break
            _msg = QMessageBox()
            _msg.setWindowTitle('Сообщение')
            _msg.setText('Выберите файл Y')
            _msg.exec_()
            file_path_2 = QFileDialog.getOpenFileName(self, 'Select Folder', filter="*.csv")[0]
            if not os.path.exists(file_path_2):
                break

            obj = iterators.DateIteratorXY(file_path_1, file_path_2)
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
            i = i + 1

    def start_iter_year(self):
        i = 1
        while i < 2:
            _msg = QMessageBox()
            _msg.setWindowTitle('Сообщение')
            _msg.setText('Выберите директорию датасета разбитого по годам')
            _msg.exec_()
            file_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
            if not os.path.exists(file_path):
                break
            obj = iterators.DateIteratorYearOrWeek(file_path)

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
            i = i + 1

    def start_iter_week(self):
        i = 1
        while i < 2:
            _msg = QMessageBox()
            _msg.setWindowTitle('Сообщение')
            _msg.setText('Выберите директорию датасета разбитого по неделям')
            _msg.exec_()
            file_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
            if not os.path.exists(file_path):
                break
            obj = iterators.DateIteratorYearOrWeek(file_path)

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
            i = i + 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GismeteoApplication()
    sys.exit(app.exec_())
