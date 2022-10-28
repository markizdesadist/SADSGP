from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt
from abc import ABC, abstractmethod


# ======================================


class BaseBtn(ABC):
    def __init__(self):
        super(BaseBtn, self).__init__()
        self.btn = QPushButton()
        self.action()
        self.setting_btn()

    def set_button(self):
        return self.btn

    @abstractmethod
    def setting_btn(self):
        pass

    @abstractmethod
    def action(self):
        pass


# ======================================

class BtnSave(BaseBtn):
    def __init__(self):
        super(BtnSave, self).__init__()
        pass

    def setting_btn(self):
        self.btn.setText('Сохранить')

    def action(self):
        pass

    def act(self):
        pass


# ======================================

class BtnExit(BaseBtn):
    def __init__(self):
        super(BtnExit, self).__init__()
        pass

    def setting_btn(self):
        self.btn.setText('Выход')

    def action(self):
        self.btn.clicked.connect(lambda: print('Exit'))


# ======================================

class BtnPrint(BaseBtn):
    def __init__(self):
        super(BtnPrint, self).__init__()
        pass

    def setting_btn(self):
        self.btn.setText('Печать')

    def action(self):
        self.btn.clicked.connect(lambda: print('Печать'))


# ======================================

class BtnRefresh(BaseBtn):
    def __init__(self):
        super(BtnRefresh, self).__init__()
        pass

    def setting_btn(self):
        self.btn.setText('Очистить')

    def action(self):
        self.btn.clicked.connect(lambda: print('Очистить'))


if __name__ == '__main__':
    pass
