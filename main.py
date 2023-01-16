import sys
from PyQt5.QtWidgets import QApplication
from winstart.winstarter import start, MainWindow

if __name__ == '__main__':
    start_app = QApplication(sys.argv)
    windows = MainWindow()
    start(windows)
    sys.exit(start_app.exec_())
