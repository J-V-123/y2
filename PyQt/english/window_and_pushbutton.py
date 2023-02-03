import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Example_window(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Button', self)   # creating a button object and placing it to the window
        self.show()                                 # displaying the window (QWidget) on the screen


if __name__ == '__main__':
    app = QApplication(sys.argv)  # creating the application object
    example = Example_window() # creating a window from our own class
    sys.exit(app.exec())
