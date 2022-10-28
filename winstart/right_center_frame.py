from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QListWidget, QLabel, QGroupBox, QFrame, QAbstractItemView, \
    QCompleter, QLineEdit
from PyQt5.QtCore import QRect, Qt


class BaseClassWidget(ABC):
    """Базовый класс для создания виджета ListWidget."""

    def __init__(self):
        self.data_list = list()
        self.lbl_group = QGroupBox()
        self.lbl = QLabel()
        self.find = QLineEdit()
        self.btn_refresh = QPushButton()
        self.widget_list = QListWidget()
        self.settings_elements()
        self.completer = QCompleter(self.data_list)
        self.find.setCompleter(self.completer)

    def set_body(self):
        self.vmain = QVBoxLayout()
        self.vmain.addWidget(self.lbl)
        self.vmain.addWidget(self.find)
        self.vmain.addWidget(self.widget_list)
        self.vmain.addWidget(self.btn_refresh)

        return self.vmain

    def settings_elements(self):
        self.setting_list()
        self.setting_find()
        self.setting_refresh()
        self.add_action()

        self.set_label_text()

    def setting_list(self):
        # self.list.setGeometry(QtCore.QRect(0, 0, self.size, 557))
        self.widget_list.setMinimumWidth(200)
        # self.list.setMaximumSize(QtCore.QSize(self.size, 16777215))
        # font = QtGui.QFont()
        # font.setPointSize(font_size)
        # font.setBold(bool(font_bold))
        # self.list.setFont(font)
        self.widget_list.setAutoFillBackground(True)
        self.widget_list.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.widget_list.setFrameShape(QFrame.WinPanel)
        self.widget_list.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.widget_list.setTabKeyNavigation(True)
        self.widget_list.setProperty("showDropIndicator", False)
        self.widget_list.setAlternatingRowColors(True)
        self.widget_list.setSelectionBehavior(QAbstractItemView.SelectRows)

    def setting_find(self):
        # self.completer = QCompleter(self.temp_list)

        self.lbl.setGeometry(QRect(0, 0, 200, 30))
        # self.label_list.setFont(CSS.set_font(14))
        self.lbl.setAutoFillBackground(False)
        self.lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lbl.setAlignment(Qt.AlignCenter)
        # self.label_list.setCompleter(self.completer)

    def setting_refresh(self):
        self.btn_refresh.setGeometry(QRect(70, 0, 117, 30))
        # self.btn_pushButton_update.setFont(CSS.set_font())
        self.btn_refresh.setAutoFillBackground(False)
        self.btn_refresh.setStyleSheet("background-color: rgb(0, 170, 0);\n"
                                       "border-bottom-color: rgb(255, 255, 127);")
        self.btn_refresh.setText('Обновить')

    def set_item(self, text_a):
        """Запись одного элемента в ListWidget."""
        self.widget_list.addItem(text_a)

    def set_items(self, list_a):
        """Запись списка элементов в ListWidget."""
        for elem in list_a:
            self.widget_list.addItem(str(elem))

    def clear_items(self):
        """Очистка поля ListWidget."""
        self.widget_list.clear()

    def add_action(self):
        """Назначение действия кнопки обновления для ListWidget."""
        self.btn_refresh.clicked.connect(lambda: self.print())

    @abstractmethod
    def get_item_text_from_list(self, *args):
        pass

    @abstractmethod
    def print(self):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в поле ListWidget."""
        self.clear_items()
        self.set_items(self.data_list)

    @abstractmethod
    def print_widget(self, *args):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в соседствующие поля ListWidget."""
        pass

    @abstractmethod
    def print_one(self, *args):
        pass

    @abstractmethod
    def set_label_text(self):
        pass


# ===============================================
class ListOrder(BaseClassWidget):
    list = [str(x) for x in ['q', 'w', 'e', 'r']]

    def __init__(self):
        super(ListOrder, self).__init__()
        self.data_list = [str(x) for x in ['q', 'w', 'e', 'r']]

        self.print()

    def set_label_text(self, text: str = None, car: str = None):
        if text and car:
            self.lbl.setText('Открытые акты клиента {text} на машину {car}'.format(text=text, car=car))
        elif text and not car:
            self.lbl.setText('Открытые акты клиента {text}'.format(text=text))
        else:
            self.lbl.setText('Открытые акты')

    def get_item_text_from_list(self, *args):
        pass

    def print(self):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в поле ListWidget."""
        # self.clear_items()
        # self.set_items(self.data_list)
        pass

    def print_widget(self, *args):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в соседствующие поля ListWidget."""
        pass

    def print_one(self, *args):
        pass


# ===============================================
class ListCar(BaseClassWidget):
    list = [str(x) for x in ['Volvo', 'MAZ', 'Mazda', 'DAF']]

    def __init__(self):
        super(ListCar, self).__init__()
        self.data_list = [str(x) for x in ['Volvo', 'MAZ', 'Mazda', 'DAF']]

        self.print()

    def set_label_text(self, text: str = None):
        if text:
            self.lbl.setText('Машины клиента {text}'.format(text=text))
        else:
            self.lbl.setText('Список техники')

    def get_item_text_from_list(self, *args):
        pass

    def print(self):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в поле ListWidget."""
        self.clear_items()
        self.set_items(self.data_list)

    def print_widget(self, *args):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в соседствующие поля ListWidget."""
        pass

    def print_one(self, *args):
        pass


# ===============================================
class ListClient(BaseClassWidget):
    list = [str(x) for x in range(10)]

    def __init__(self):
        super(ListClient, self).__init__()
        self.data_list = [str(x) for x in range(20, 40)]

        self.print()

    def set_label_text(self):
        self.lbl.setText('Список клиентов')

    def get_item_text_from_list(self, *args):
        pass

    def print(self):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в поле ListWidget."""
        self.clear_items()
        self.set_items(self.data_list)

    def print_widget(self, *args):
        """Переназначаемая функция. Очистка поля и добавление элементов списка в соседствующие поля ListWidget."""
        pass

    def print_one(self, *args):
        pass


if __name__ == "__main__":
    pass
