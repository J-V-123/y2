import sys
from PyQt6 import QtWidgets
from mainwindow import MainWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Launch an instance of QApplication
    window = MainWindow()
    sys.exit(app.exec())  # Start the Qt event loop
