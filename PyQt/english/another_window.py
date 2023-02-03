import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6 import QtGui


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.label = QLabel("Hello world!")
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)


class Main_Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.window = None  # creating an attribute to use for checking if the window is already created to avoid creating several windows
        self.label = QLabel("Open new window")  # creating a label
        self.button = QPushButton("Open")  # creating a button

        self.layout = QVBoxLayout()  # creating a layout
        self.layout.addWidget(self.label)  # adding the label to the layou
        self.layout.addWidget(self.button)  # adding the button to the layout

        self.central_widget = QWidget()  # creating a QWidget to be the central widget
        self.central_widget.setLayout(self.layout)  # setting a layout for it
        self.setCentralWidget(self.central_widget)  # setting it to the central widget

        self.button.clicked.connect(self.show_window)  # connecting clicking the button to the show_window() method
        self.show()  # displaying the main window

    def show_window(self):
        # if self.window is None: # checking if the window is already created
        self.window = Window()  # creating the window
        self.window.show()  # d displaying the window

    def closeEvent(self, a0: QtGui.QCloseEvent):  # closing the window if the main window gets closed
        if self.window:
            self.window.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # creating the application object
    main_window = Main_Window()
    sys.exit(app.exec())
