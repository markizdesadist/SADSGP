#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'DeathAdder'

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QFrame, QVBoxLayout, QTabWidget, QLabel, QWidget, QDialog
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore, QtGui
from winstart.splashscreen import splasher
from winstart.order_frame import Order, Client, Car
from winstart.right_center_frame import ListClient, ListOrder, ListCar
from winstart.button_frame import BtnSave, BtnExit, BtnPrint, BtnRefresh
from winstart.upper_frame import Logo

from setting import logger
import sys
import os


class Command:
    def __init__(self):
        self.order = Order()
        self.car = Car()
        self.client = Client()

        self.list_order = ListOrder()
        self.list_car = ListCar()
        self.list_client = ListClient()

        self.btn_save = BtnSave()
        self.btn_refresh = BtnRefresh()
        self.btn_print = BtnPrint()
        self.btn_exit = BtnExit()

        self.logo = Logo()

        self.add_action()

    def foo(self):
        try:
            a = 1 / 0
        except ZeroDivisionError as err:
            Dialog().on_clicked()

    def add_action(self):
        self.btn_save.btn.clicked.connect(lambda: self.order.car_edit.brand[1].setText('123123123'))
        self.btn_refresh.btn.clicked.connect(lambda: Dialog().on_clicked())
        self.btn_print.btn.clicked.connect(lambda: self.foo())


# =============================================================================

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()

    def on_clicked(self):
        dialog = self
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            print("Нажата кнопка ОК")
            # Здесь получаем данные из диалогового окна
        else:
            print("Нажата кнопка Cancel")

class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.commands = Command()
        self.root_frame = QtWidgets.QVBoxLayout(self)
        self.upper_frame = QtWidgets.QHBoxLayout()
        self.center_frame = QtWidgets.QHBoxLayout()
        self.lower_frame = QtWidgets.QHBoxLayout()
        self.tabWidget = QTabWidget()
        self.set_tab()
        self.left_main = QVBoxLayout()
        self.lower_lbl = QLabel()
        self.button_frame = QFrame()
        self.main_btn = QHBoxLayout(self.button_frame)
        self.right_main = QHBoxLayout()

    @logger.logger.catch
    def setting_window(self):
        """
        Настройки основного окна.
        :return: None
        """
        self.setObjectName("MainWindow")
        self.setWindowTitle("Пробная кукушка")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.Window)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(os.path.join(os.getcwd(), '..', 'templatefiles', 'lpgo.jpg')),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On
        )
        self.setWindowIcon(icon)
        # self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setMinimumSize(650, 900)
        self.resize(1500, 800)
        self.setAutoFillBackground(True)
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)

        self.ui_window()
        """
        Размещение окна по центру:
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)"""

    @logger.logger.catch
    def ui_window(self):
        self.root_frame.insertLayout(0, self.commands.logo.set_frame())
        self.root_frame.insertLayout(1, self.center_frame)
        # self.root_frame.insertWidget(2, button_frame.BtnFrame().set_frame())

        self.center_frame.addLayout(self.set_frame_left())
        self.center_frame.addLayout(self.set_frame_right())

    # ======================================================================================

    def set_frame_right(self):
        """Установка фрейма виджета."""

        self.right_main.addLayout(self.commands.list_client.set_body())
        self.right_main.addLayout(self.commands.list_car.set_body())
        self.right_main.addLayout(self.commands.list_order.set_body())

        return self.right_main

    # ==================================================================================

    def set_frame_btn(self):
        self.button_frame.setMaximumWidth(598)
        self.button_frame.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.main_btn.addWidget(self.commands.btn_refresh.set_button(), alignment=Qt.AlignRight)
        self.main_btn.addWidget(self.commands.btn_save.set_button(), alignment=Qt.AlignRight)
        self.main_btn.addWidget(self.commands.btn_print.set_button(), alignment=Qt.AlignRight)
        self.main_btn.addWidget(self.commands.btn_exit.set_button(), alignment=Qt.AlignRight)
        return self.button_frame

    # ==================================================================================
    def set_tab(self):
        self.tabWidget.setMaximumSize(600, 700)
        self.tabWidget.setMinimumSize(600, 700)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)

        self.tabWidget.addTab(self.commands.order.set_frame(), '')
        self.tabWidget.addTab(self.commands.client.set_frame(), '')
        self.tabWidget.addTab(self.commands.car.set_frame(), '')

        self.tab_old_order = QWidget()
        self.tab_old_order.setObjectName('tab_old_order')
        self.tabWidget.addTab(self.tab_old_order, '')

        self.tab_help = QWidget()
        self.tab_help.setObjectName('tab_help')
        self.tabWidget.addTab(self.tab_help, '')

        self.tabWidget.setTabText(0, 'Печать Актов')
        self.tabWidget.setTabText(1, 'Новый клиент')
        self.tabWidget.setTabText(2, 'Новая машина')
        self.tabWidget.setTabText(3, 'Закрытые акты')
        self.tabWidget.setTabText(4, 'Справка')

        self.tabWidget.setCurrentIndex(0)

    def set_frame_left(self):
        self.lower_lbl.setText('123123123')
        self.lower_lbl.setMinimumHeight(23)
        self.lower_lbl.setStyleSheet("background-color: rgb(0, 170, 0);")

        self.left_main.addWidget(self.tabWidget, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.left_main.addWidget(self.set_frame_btn())
        self.left_main.addWidget(self.lower_lbl, alignment=Qt.AlignBottom)

        return self.left_main

    # ======================================================================================


@splasher
def start(win):
    logger.logger.info(': Начал работу с программой.')
    win.setting_window()
    win.show()


if __name__ == '__main__':
    start_app = QApplication(sys.argv)
    windows = MainWindow()
    start(windows)
    sys.exit(start_app.exec_())
