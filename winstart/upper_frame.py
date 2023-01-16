from PyQt5.QtWidgets import QHBoxLayout, QLabel, QTimeEdit, QAbstractSpinBox
from PyQt5.QtCore import Qt, QSize, QTime, QTimer, QRect
from datetime import datetime


class Logo:
    def __init__(self):
        self.lbl = QLabel()
        self.timer = Timer().set_timer()
        self.settings_elements()

    def settings_elements(self):
        self.settings_label()
        self.set_logo_text()


    def set_frame(self):
        self.hmain = QHBoxLayout()
        self.hmain.addWidget(self.lbl, alignment=Qt.AlignCenter)
        self.hmain.addWidget(self.timer, alignment=Qt.AlignRight | Qt.AlignVCenter)
        return self.hmain

    def set_logo_text(self, text: str = 'ЛОГОТИП'):
        self.lbl.setText(text)

    def settings_label(self):
        self.lbl.setMinimumWidth(50)
        self.lbl.setMaximumWidth(50)


class Timer:
    def __init__(self):
        self.timeEdit = QTimeEdit()
        self.current_time = QTime.currentTime()
        self.timer = QTimer()

    def set_timer(self):
        # self.timeEdit.setGeometry(QRect(50, 0, 150, 70))
        size = QSize(300, 50)
        size.scale(200, 50, Qt.KeepAspectRatio)
        self.timeEdit.setMinimumSize(size)
        self.timeEdit.setMaximumSize(size)
        self.timeEdit.setLayoutDirection(Qt.LeftToRight)
        self.timeEdit.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.timeEdit.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEdit.setKeyboardTracking(False)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setTime(datetime.now().time())

        self.timer.timeout.connect(self.time_edit_update)
        self.timer.start(1000)

        return self.timeEdit

    def time_edit_update(self):
        self.timeEdit.setTime(self.current_time)


if __name__ == '__main__':
    pass

