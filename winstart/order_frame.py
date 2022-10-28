import os
from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QHBoxLayout, QFormLayout, \
    QLabel, QGridLayout, QFrame, QWidget, QCompleter, QRadioButton, QCheckBox, \
    QAbstractSpinBox, QDateEdit, QLCDNumber
from PyQt5.QtCore import QRect, Qt, QSize
from PyQt5.QtGui import QPixmap

from datetime import datetime
from random import choice as rand_choice


class BaseTabFrame(ABC):
    def __init__(self):
        super(BaseTabFrame, self).__init__()
        self.widget = QWidget()
        self.grid_frame = QGridLayout(self.widget)
        self.vmain = QVBoxLayout()
        self.hmain = QHBoxLayout()
        self.car_edit = CarLabelGroup()
        self.client_edit = ClientLabelGroup()
        self.driver = DriverLabelGroup()
        self.check_box = CheckBoxOrder()
        self.calendar = Calendar()
        self.lcd_number = LcdOrderNumber()
        self.logo = self.set_logo()
        self.rand_img = self.set_maz_img()
        self.line = self.line_tab()
        self.num_form = QFormLayout()

        self.set_pattern()

    def set_pattern(self):
        self.num_form.addRow('номер акта', self.lcd_number.set_lcd())

        self.hmain.addWidget(self.set_logo(), alignment=Qt.AlignLeft | Qt.AlignTop)
        self.hmain.addWidget(self.calendar.set_datetime(), alignment=Qt.AlignCenter | Qt.AlignTop)
        self.hmain.addLayout(self.num_form, stretch=0)

        self.grid_frame.addLayout(self.hmain, 0, 0, 1, 3, alignment=Qt.AlignTop)
        self.grid_frame.addWidget(self.calendar.set_datetime(), 0, 1, 1, 1, alignment=Qt.AlignCenter)
        self.grid_frame.addWidget(self.line_tab(), 1, 0, 1, 3, alignment=Qt.AlignLeft)
        self.grid_frame.addWidget(self.line_tab(), 4, 0, 1, 3, alignment=Qt.AlignLeft)
        self.grid_frame.addWidget(self.set_maz_img(), 8, 0, 1, 3, alignment=Qt.AlignCenter | Qt.AlignBottom)

    @abstractmethod
    def set_frame(self):
        pass

    @classmethod
    def set_maz_img(cls):
        path_img = os.path.join('..', 'templatefiles', 'IMG_maz')
        if not os.path.exists(path_img):
            os.mkdir(path_img)

        img_list = [
            os.path.sep.join(
                (
                    path_img,
                    elem
                )
            )
            for elem
            in os.listdir(path_img)
            if elem.endswith('.jpg')
        ]

        rand_img = QLabel()
        rand_img.setBaseSize(433, 120)
        rand_img.setMaximumHeight(300)
        rand_img.setPixmap(
            QPixmap(
                '{}'.format(
                    rand_choice(img_list)
                )
            ).scaledToWidth(rand_img.width())
        )

        return rand_img

    @classmethod
    def set_logo(cls):
        logo = QLabel()
        logo.setGeometry(5, 5, 90, 90)
        logo.setPixmap(
            QPixmap(
                '{}'.format(
                    os.path.join('..', 'templatefiles', 'logo.jpg')
                )
            ).scaledToWidth(logo.width())
        )
        return logo

    @classmethod
    def line_tab(cls):
        line = QFrame()
        line.setMaximumSize(QSize(550, 10))
        line.setMinimumSize(QSize(550, 10))
        line.setStyleSheet("background-color: rgb(251, 251, 251);\nborder-color: rgb(251, 251, 251);")
        line.setLineWidth(3)
        line.setAutoFillBackground(False)
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        return line


# =======================================

class Order(BaseTabFrame):
    def __init__(self):
        super(Order, self).__init__()

    def set_frame(self):
        self.grid_frame.addWidget(self.client_edit.set_group(), 2, 0, 1, 3, alignment=Qt.AlignLeft)
        self.grid_frame.addWidget(self.driver.set_group(), 3, 0, 1, 3, alignment=Qt.AlignLeft)
        self.grid_frame.addWidget(self.car_edit.set_group(), 5, 0, 1, 3, alignment=Qt.AlignLeft)
        self.grid_frame.addWidget(self.check_box.set_group(), 6, 1, 1, 2, alignment=Qt.AlignLeft)
        self.grid_frame.addWidget(self.line_tab(), 7, 0, 1, 3, alignment=Qt.AlignLeft)

        return self.widget


# =======================================

class Car(BaseTabFrame):
    def __init__(self):
        super(Car, self).__init__()

    def set_frame(self):
        self.car_edit.brand[1].setReadOnly(False)
        self.car_edit.model[1].setReadOnly(False)
        self.car_edit.number[1].setReadOnly(False)
        self.car_edit.year[1].setReadOnly(False)
        self.car_edit.code[1].setReadOnly(False)

        self.car_edit.brand[1].setStyleSheet("background-color: LightSeaGreen;")
        self.car_edit.model[1].setStyleSheet("background-color: LightSeaGreen;")
        self.car_edit.number[1].setStyleSheet("background-color: LightSeaGreen;")
        self.car_edit.year[1].setStyleSheet("background-color: LightSeaGreen;")
        self.car_edit.code[1].setStyleSheet("background-color: LightSeaGreen;")

        self.grid_frame.addWidget(self.client_edit.set_group(), 2, 0, 1, 3, alignment=Qt.AlignLeft | Qt.AlignTop)
        self.grid_frame.addWidget(self.car_edit.set_group(), 5, 0, 1, 3, alignment=Qt.AlignLeft | Qt.AlignBottom)
        self.grid_frame.removeWidget(self.set_maz_img())

        return self.widget


# =======================================

class Client(BaseTabFrame):
    def __init__(self):
        super(Client, self).__init__()

    def set_frame(self):
        self.client_edit.name[1].setReadOnly(False)
        self.client_edit.fname[1].setReadOnly(False)
        self.client_edit.address[1].setReadOnly(False)
        self.client_edit.phone[1].setReadOnly(False)
        self.client_edit.code[1].setReadOnly(False)

        self.client_edit.name[1].setStyleSheet("background-color: LightSeaGreen;")
        self.client_edit.fname[1].setStyleSheet("background-color: LightSeaGreen;")
        self.client_edit.address[1].setStyleSheet("background-color: LightSeaGreen;")
        self.client_edit.phone[1].setStyleSheet("background-color: LightSeaGreen;")
        self.client_edit.code[1].setStyleSheet("background-color: LightSeaGreen;")

        self.grid_frame.addWidget(self.client_edit.set_group(), 2, 0, 1, 3, alignment=Qt.AlignLeft | Qt.AlignTop)
        # self.grid_frame.re

        return self.widget


# =======================================

class OldOrder(BaseTabFrame):
    def __init__(self):
        super(OldOrder, self).__init__()


# =======================================
label_dict = {
    'CarLabelGroup': {
        'brand': 'Марка машины',
        'model': 'Модель машины',
        'number': 'Номер машины',
        'year': 'Год выпуска ',
        'code': 'УЗМ код машины'
    },
    'ClientLabelGroup': {
        'name': 'Название клиента',
        'fname': 'Полное название',
        'address': 'Адрес клиента',
        'code': 'УНП клиента',
        'phone': 'Номера телефонов'
    },
    'DriverLabelGroup': {
        'name': 'ФИО заказчика',
        'job': 'Должность',
    }
}


class BaseLabelGroup(ABC):

    def __init__(self):
        self.element = QLineEdit()

        self.completer_list = list()
        completer = QCompleter(self.completer_list)
        self.element.setCompleter(completer)

    @classmethod
    def set_form(cls, temp_tuple: tuple, flag: bool = False):
        form = QFormLayout()
        if flag:
            form.addRow(temp_tuple[1], temp_tuple[0])
        else:
            form.addRow(temp_tuple[0], temp_tuple[1])
        return form

    @abstractmethod
    def set_group(self):
        pass

    def set_elem(self, text: str):
        self.element = QLineEdit()
        self.element.setReadOnly(True)
        self.element.setStyleSheet("background-color: Grey;")

        temp_label = QLabel()
        self.element.setGeometry(QRect(128, 190, 425, 31))
        self.element.setAutoFillBackground(True)
        self.element.setClearButtonEnabled(True)
        self.element.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.element.setPlaceholderText(text)

        temp_label.setGeometry(QRect(128, 350, 181, 30))
        # self.txt_label_brand.setFont(CSS.set_font(12, False, 50))
        temp_label.setText(text)
        temp_label.setAutoFillBackground(False)
        temp_label.setStyleSheet("background-color: rgb(221, 221, 221);")
        temp_label.setMargin(5)

        return temp_label, self.element


class CarLabelGroup(BaseLabelGroup):
    def __init__(self):
        super(CarLabelGroup, self).__init__()
        self.replacement_part = QRadioButton('Запчасти')
        self.machine = QRadioButton('Машина')
        self.trailer = QRadioButton('прицеп')

        self.brand = self.set_elem(label_dict[self.__class__.__name__]['brand'])
        self.model = self.set_elem(label_dict[self.__class__.__name__]['model'])
        self.number = self.set_elem(label_dict[self.__class__.__name__]['number'])
        self.year = self.set_elem(label_dict[self.__class__.__name__]['year'])
        self.code = self.set_elem(label_dict[self.__class__.__name__]['code'])

    def set_group(self):
        self.year[1].setMaxLength(4)
        self.main = QFrame()
        self.main.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.main.setMaximumHeight(150)
        self.form = QGridLayout()
        self.form.addWidget(self.replacement_part, 0, 0, 1, 1, alignment=Qt.AlignTop)
        self.form.addWidget(self.machine, 0, 1, 1, 1, alignment=Qt.AlignTop)
        self.form.addWidget(self.trailer, 0, 2, 1, 1, alignment=Qt.AlignTop)

        self.form.addLayout(self.set_form(self.brand), 1, 0, 1, 1, alignment=Qt.AlignBottom)
        self.form.addLayout(self.set_form(self.model, True), 1, 1, 1, 2)
        self.form.addLayout(self.set_form(self.number), 2, 0, 1, 1)
        self.form.addLayout(self.set_form(self.year, True), 2, 1, 1, 2)
        self.form.addLayout(self.set_form(self.code), 3, 0, 1, 2)
        self.main.setLayout(self.form)

        return self.main


# =======================================

class ClientLabelGroup(BaseLabelGroup):
    def __init__(self):
        super(ClientLabelGroup, self).__init__()
        self.name = self.set_elem(label_dict[self.__class__.__name__]['name'])
        self.fname = self.set_elem(label_dict[self.__class__.__name__]['fname'])
        self.address = self.set_elem(label_dict[self.__class__.__name__]['address'])
        self.code = self.set_elem(label_dict[self.__class__.__name__]['code'])
        self.phone = self.set_elem(label_dict[self.__class__.__name__]['phone'])

    def set_group(self):
        self.code[1].setMaxLength(9)
        self.main = QFrame()
        self.main.setMaximumHeight(150)
        self.main.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.form = QGridLayout()
        self.form.addLayout(self.set_form(self.name), 0, 0, 1, 1, alignment=Qt.AlignBottom)
        self.form.addLayout(self.set_form(self.code), 0, 1, 1, 1)
        self.form.addLayout(self.set_form(self.fname), 1, 0, 1, 2)
        self.form.addLayout(self.set_form(self.address), 2, 0, 1, 2)
        self.form.addLayout(self.set_form(self.phone), 3, 0, 1, 2)
        self.main.setLayout(self.form)

        return self.main


# =======================================

class DriverLabelGroup(BaseLabelGroup):
    def __init__(self):
        super(DriverLabelGroup, self).__init__()
        self.name = self.set_elem(label_dict[self.__class__.__name__]['name'])
        self.job = self.set_elem(label_dict[self.__class__.__name__]['job'])

    def set_group(self):
        self.main = QFrame()
        self.main.setMaximumHeight(150)
        self.main.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.form = QGridLayout()
        self.name[1].setStyleSheet("background-color: LightSeaGreen;")
        self.job[1].setStyleSheet("background-color: LightSeaGreen;")
        self.name[1].setReadOnly(False)
        self.job[1].setReadOnly(False)

        self.form.addLayout(self.set_form(self.name), 0, 0, 1, 1, alignment=Qt.AlignBottom)
        self.form.addLayout(self.set_form(self.job, True), 0, 1, 1, 1)
        self.main.setLayout(self.form)

        return self.main


class CheckBoxOrder:
    def __init__(self):
        self.first = QCheckBox('Заказ')
        self.second = QCheckBox("Наряд")
        self.third = QCheckBox("Внутренний")
        self.fourth = QCheckBox("Для работы")

        self.settings_elements()

    def settings_elements(self):
        self.first.setChecked(True)
        self.second.setChecked(True)
        self.third.setChecked(True)
        self.fourth.setChecked(True)

    def set_group(self):
        self.main = QFrame()
        self.main.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.main.setMaximumHeight(150)
        self.form = QGridLayout()

        self.form.addWidget(self.first, 0, 0, 1, 1, alignment=Qt.AlignBottom)
        self.form.addWidget(self.second, 0, 1, 1, 1, alignment=Qt.AlignBottom)
        self.form.addWidget(self.third, 1, 0, 1, 1, alignment=Qt.AlignBottom)
        self.form.addWidget(self.fourth, 1, 1, 1, 1, alignment=Qt.AlignBottom)
        self.main.setLayout(self.form)

        return self.main


class Calendar:
    def __init__(self):
        self.dateEdit = QDateEdit()

    def set_datetime(self):
        self.dateEdit.setDate(datetime.now())
        self.dateEdit.setBaseSize(100, 50)
        self.dateEdit.setDisplayFormat('dd . MMMM . yyyy')
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.dateEdit.setProperty('showGroupSeparator', True)
        self.dateEdit.setCalendarPopup(True)

        return self.dateEdit


class LcdOrderNumber:
    def __init__(self):
        self.lsd = QLCDNumber(8)

    def set_lcd(self):
        self.lsd.display('001 - A')
        self.lsd.setSegmentStyle(QLCDNumber.Flat)
        self.lsd.setDecMode()

        return self.lsd


# class RadioBtn:
#     def __init__(self):
#
#
# def set_radio(self):
#     self.main = QFrame()
#     self.main.setFrameStyle(QFrame.Panel | QFrame.Raised)
#     self.main.setMaximumHeight(150)
#     self.form = QGridLayout()
#
#     self.form.addWidget(self.replacement_part, 1, 0, 1, 1, alignment=Qt.AlignTop)
#     self.form.addWidget(self.machine, 1, 0, 1, 1, alignment=Qt.AlignTop)
#     self.form.addWidget(self.trailer, 1, 0, 1, 1, alignment=Qt.AlignTop)
#     self.main.setLayout(self.form)
#
#     return self.main

if __name__ == '__main__':
    ord = BaseTabFrame()
    print(ord)
