import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 100) # setting the size of the window
        self.label = QLabel(self)  # creating an empty label
        self.label.setStyleSheet("background-color : pink;")  # setting a background color for the label. The string is of css language
        self.show()  # näytetään määrittelyt näytölle

    def keyPressEvent(self, event):  # overwriting the keyPressEvent() method written in the QWidget class so that the program can react to pressing keys
        if event.key() == Qt.Key.Key_T:  # if the key of the event object the method got as a parameter was T
            self.label.setText("You pressed the key T") # The text of the label is set
        elif event.key() == Qt.Key.Key_Y:
            self.label.setText("You pressed the key Y")
        else:
            self.label.setText("You pressed some key that is not T or Y")
        self.label.adjustSize()  # adjusting the size of the label so that the text will fit in the label


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
