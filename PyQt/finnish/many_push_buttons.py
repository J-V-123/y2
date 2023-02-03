import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton  # tuodaan käytettävät luokat sovelluksen käytettäväksi


class Example_window(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton('Button', self)       # luodaan nappula
        self.button2 = QPushButton('Button2', self)     # luodaan toinen napppula
        self.button2.move(20, 60)                     # siirretään nappulaa 20 pikseliä x-akselilla ja 60 pixeliä y-akselilla. Kun tämä rivi on kommentoituna, nappulat asettuvat päällekäin
        self.show()                                     # Päivittää ylläolevat määrittelyt näkymään ruudulle


if __name__ == '__main__':
    app = QApplication(sys.argv)                       # Luodaan QApplication-objekti
    example = Example_window()                         # Luodaan ikkuna
    sys.exit(app.exec())                               # app.exec_() aloittaa tapahtumankäsittelyn
