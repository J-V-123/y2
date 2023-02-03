import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout  # tuodaan käytettävät luokat sovelluksen käytettäväksi


class Example_mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('1')     # creating a button with the text '1'
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')

        self.main_widget = QWidget()   # creating a widget to be a central widget
        self.setCentralWidget(self.main_widget) #setting the widget to central widget

        self.main_layout = QVBoxLayout()    # creating a vertical layout box to be the central layout
        self.red_layout1 = QVBoxLayout()    # creating a vertical layout box to put inside the central layout
        self.red_layout2 = QHBoxLayout()    # creating a horizontal layout box to put inside the central layout

        self.main_layout.addLayout(self.red_layout1)  # putting the second vertical layout box inside the first vertical layout box
        self.main_layout.addLayout(self.red_layout2)

        self.red_layout1.addWidget(self.button1)   # adding the first button inside the vertical layout box
        self.red_layout1.addWidget(self.button2)

        self.red_layout2.addWidget(self.button3)   # adding the third button inside the horizontal layout box
        self.red_layout2.addWidget(self.button4)

        self.main_widget.setLayout(self.main_layout)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # creating the application object
    example = Example_mainwindow()
    sys.exit(app.exec())
