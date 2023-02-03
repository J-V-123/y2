import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QGridLayout

class Example_mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('1')                     # luodaan nappula tekstillä '1'
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')

        self.main_widget = QWidget()                        # luodaan QWidget
        self.setCentralWidget(self.main_widget)             # asetetaan pääikkunalle pääwidget

        self.gridlayout = QGridLayout()                     # luodaan ruudukko-asettelu

        self.gridlayout.addWidget(self.button1, 1, 1)       # lisätään nappula 1 ruutuun (1, 1)
        self.gridlayout.addWidget(self.button2, 1, 2)
        self.gridlayout.addWidget(self.button3, 2, 1)
        self.gridlayout.addWidget(self.button4, 2, 2)

        self.main_widget.setLayout(self.gridlayout)         # asetetaan pääwidgetille asettelu

        self.show()                                         # Päivittää ylläolevat määrittelyt näkymään ruudulle

if __name__ == '__main__':
    app = QApplication(sys.argv)                            # Luodaan QApplication-objekti
    example = Example_mainwindow()
    sys.exit(app.exec())                                    # app.exec_() aloittaa tapahtumankäsittelyn, joka päättyy kun sovellus suljetaan. sys.exit() huolehtii siitä, että sovellus sulkeutuu "siististi".
