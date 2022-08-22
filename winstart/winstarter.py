# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from winstart.right_center_frame import RightCentralWidget
from winstart.left_center_frame import LeftCentralWidget
from winstart.upper_frame import Logo
from setting import logger
import sys
import os
import time


class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.root_frame = QtWidgets.QVBoxLayout(self)
        self.upper_frame = QtWidgets.QHBoxLayout()
        self.center_frame = QtWidgets.QHBoxLayout()
        self.lower_frame = QtWidgets.QHBoxLayout()


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
        self.root_frame.insertLayout(0, Logo().set_frame())
        self.root_frame.insertLayout(1, self.center_frame)
        # self.root_frame.insertWidget(2, button_frame.BtnFrame().set_frame())

        self.center_frame.addLayout(LeftCentralWidget().set_frame())
        self.center_frame.addLayout(RightCentralWidget().set_frame())


""" @@@@@@@@@@@@@@@@@@@@@@@@   DialogScreen        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  """

""" @@@@@@@@@@@@@@@@@@@@@@@@   SplashScreen        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  """


def splasher(func):
    # @wraps
    def wrapper(*args, **kwargs):
        def load_data(sp):
            for i in range(1, 3):
                time.sleep(1)
                sp.showMessage(
                    "Загрузка данных ... 0%",
                    QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom,
                    QtCore.Qt.red
                )
                QtWidgets.qApp.processEvents()

        splash = QtWidgets.QSplashScreen(QtGui.QPixmap(""))
        splash.showMessage(
            "Загрузка данных ... 0%",
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom,
            QtCore.Qt.white
        )
        splash.show()
        QtWidgets.qApp.processEvents()
        load_data(splash)
        splash.finish(*args)
        func(*args, **kwargs)

    return wrapper


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
