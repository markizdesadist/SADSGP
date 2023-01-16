from datetime import datetime

import os

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont

from frame.CSS_template import CSS
from log_setting import config
from log_setting import logger

text = config['HELP']['help_text']
font = QFont(config['HELP']['size_font'])
request = config['HELP']['request']


class Help:
    def __init__(self):
        self.frame_help = None
        self.txt_plainTextEdit_help = None

    def set_body(self, frame):
        self.frame_help = QtWidgets.QFrame(frame)
        self.frame_help.setGeometry(QtCore.QRect(15, 5, 571, 593))
        self.frame_help.setAutoFillBackground(True)
        self.frame_help.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_help.setObjectName("frame_help")

        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_help)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(1, 1, 569, 592))
        self.gridLayoutWidget.setAutoFillBackground(True)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget_Tab")

        self.gridLayout_listWidget_main = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_listWidget_main.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_listWidget_main.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_listWidget_main.setHorizontalSpacing(0)
        self.gridLayout_listWidget_main.setVerticalSpacing(2)
        self.gridLayout_listWidget_main.setObjectName("gridLayout_listWidget_main")
        self.gridLayout_listWidget_main.setAlignment(QtCore.Qt.AlignCenter)

        self.txt_plainTextEdit_help = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_plainTextEdit_help.setGeometry(QtCore.QRect(1, 1, 10, 10))
        self.txt_plainTextEdit_help.setAutoFillBackground(True)
        self.txt_plainTextEdit_help.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.txt_plainTextEdit_help.setObjectName("txt_plainTextEdit_help")
        self.txt_plainTextEdit_help.setFont(font)
        self.txt_plainTextEdit_help.setReadOnly(True)
        self.txt_plainTextEdit_help.insertPlainText(text)

        self.txt_plainTextEdit_request = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.txt_plainTextEdit_request.setGeometry(QtCore.QRect(1, 1, 10, 10))
        self.txt_plainTextEdit_request.setAutoFillBackground(True)
        self.txt_plainTextEdit_request.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_plainTextEdit_request.setObjectName("txt_plainTextEdit_request")
        self.txt_plainTextEdit_request.setFont(font)
        self.txt_plainTextEdit_request.setPlaceholderText('Enter request')

        self.button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button.setBaseSize(100, 35)
        self.button.setStyleSheet(CSS.set_btn_color())
        self.button.setFont(CSS.set_font_btn())
        self.button.setText('Сохранить и отправить')

        self.gridLayout_listWidget_main.addWidget(self.txt_plainTextEdit_help, 0, 0, 1, 1)
        self.gridLayout_listWidget_main.addWidget(self.txt_plainTextEdit_request, 1, 0, 1, 1)
        self.gridLayout_listWidget_main.addWidget(self.button, 2, 0, 1, 1)

        self.add_action()

    @logger.catch
    def add_action(self):
        self.button.clicked.connect(lambda: self.save_request())

    @logger.catch
    def save_request(self):
        with open(request, 'a', encoding='utf-8') as file:
            file.write("\n{}\n{}  = {}: {}\n".format(
                '-' * 20,
                os.getlogin(),
                datetime.now(),
                self.txt_plainTextEdit_request.toPlainText()
            )
            )
        self.txt_plainTextEdit_request.clear()
        logger.info('{} направил заявку'.format(os.getlogin()))


if __name__ == '__main__':
    pass
