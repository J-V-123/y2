import sys                                         # tuodaan käytettävät luokat sovelluksen käytettäväksi
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class Example_window(QWidget):

    def __init__(self):
        super().__init__()
        self.button = QPushButton('Button', self)   # luodaan nappula-olio
        self.show()                                 # Päivittää ylläolevat määrittelyt näkymään ruudulle

if __name__ == '__main__':
    app = QApplication(sys.argv)                    # Luodaan QApplication-olio
    example = Example_window()                      # luodaan ikkuna-olio määrittämästämme luokasta
    sys.exit(app.exec())                            # app.exec_() aloittaa tapahtumankäsittelyn, joka päättyy kun
                                                    # sovellus suljetaan. sys.exit() huolehtii siitä, että
                                                    # sovellus sulkeutuu "siististi".