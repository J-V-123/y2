import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Example_window(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Button', self) # creating a button
        self.button2 = QPushButton('Button2', self) #creating another button
        #self.button2.move(20, 60)  # moving the button 20 pixels on the x-axis and 60 pixels on the y-axis. When this row is commented the second button is on the top of the first button
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # creating the application object
    example = Example_window()
    sys.exit(app.exec())

