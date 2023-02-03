import sys
from PyQt6.QtWidgets import QApplication, QWidget   # tuodaan käytettävät luokat sovelluksen käytettäväksi

def create_window():
    window = QWidget()                              # Luodaan QWidget-olio ikkunaksi
    window.setWindowTitle('Hello world!')           # Asetetaan ikkunan otsikko
    window.show()                                   # Päivitetään ylläolevat määrittelyt näkymään ruudulle
    sys.exit(app.exec())                            # app.exec() aloittaa tapahtumankäsittelyn, joka päättyy kun sovellus suljetaan.
                                                    # sys.exit() huolehtii siitä, että sovellus sulkeutuu "siististi".

if __name__ == '__main__':
    app = QApplication(sys.argv)                    # Luodaan QApplication-olio
    create_window()