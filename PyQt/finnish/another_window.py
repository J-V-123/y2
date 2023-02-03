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
        # luodaan muuttuja, jotta voidaan tarkistaa onko ikkunaa jo luotu
        # ja olla luomatta samasta ikkunasta montaa kappaletta
        self.window = None
        self.label = QLabel("Open new window")        # luodaan tesktikenttä
        self.button = QPushButton("Open")             # luodaan nappula

        self.layout = QVBoxLayout()                   # luodaan asettelu
        self.layout.addWidget(self.label)             # lisätään tekstikenttä asetteluun
        self.layout.addWidget(self.button)            # lisätään nappula asetteluun

        self.central_widget = QWidget()               # luodaan QWidget pääwidgetksi
        self.central_widget.setLayout(self.layout)    # asetetaan sille asettelu
        self.setCentralWidget(self.central_widget)    # asetaan se pääwidgetiksi

        self.button.clicked.connect(self.show_window) # yhdistetään napin painnallus show_window() -funktioon
        self.show()                                   # näytetään määrittelyt näytöllä

    def show_window(self):
        if self.window is None:                       # tarkistetaan onko ikkuna-olio luotu
            self.window = Window()                    # luodaan ikkuna
        self.window.show()                            # näytetään ikkuna

    def closeEvent(self, a0: QtGui.QCloseEvent):      # Suljetaan myös avattu ikkuna, jos pääikkuna suljetaan
        if self.window:
            self.window.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Main_Window()
    sys.exit(app.exec())
