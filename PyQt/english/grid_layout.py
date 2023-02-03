import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QGridLayout  # tuodaan käytettävät luokat sovelluksen käytettäväksi


class Example_mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('1')    #creating a button with the text '1'
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')

        self.main_widget = QWidget()  # creating a widget to be a central widget
        self.setCentralWidget(self.main_widget) #setting the widget to central widget

        self.gridlayout = QGridLayout()  # creating a grid layout

        self.gridlayout.addWidget(self.button1, 1, 1) #adding the first button to the grid in the element (1,1)
        self.gridlayout.addWidget(self.button2, 1, 2)
        self.gridlayout.addWidget(self.button3, 2, 1)
        self.gridlayout.addWidget(self.button4, 2, 2)

        self.main_widget.setLayout(self.gridlayout)  #setting the created layout for the main widget

        #self.button1.setFixedSize(80, 80)   #setting a fixed size for the first button

        self.show() 


if __name__ == '__main__':
    app = QApplication(sys.argv)  
    example = Example_mainwindow()
    sys.exit(app.exec())  