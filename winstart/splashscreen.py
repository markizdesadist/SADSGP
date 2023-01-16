from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import qApp, QSplashScreen
from time import sleep


def splasher(func):
    # @wraps
    def wrapper(*args, **kwargs):
        def load_data(sp):
            for i in range(1, 3):
                sleep(1)
                sp.showMessage(
                    "Загрузка данных ... 0%",
                    Qt.AlignHCenter | Qt.AlignBottom,
                    Qt.red
                )
                qApp.processEvents()

        splash = QSplashScreen(QPixmap("templatefiles\\CZk.gif"))
        splash.showMessage(
            "Загрузка данных ... 0%",
            Qt.AlignHCenter | Qt.AlignBottom,
            Qt.white
        )
        splash.show()
        qApp.processEvents()
        load_data(splash)
        splash.finish(*args)
        func(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    pass
