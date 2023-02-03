import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QInputDialog

class Example_mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('Show name input', self)     # luodaan nappula

        # yhdistetään nappulan painaminen dialogin avaamiseen
        self.button1.clicked.connect(self.show_dialog)

        self.label = QLabel()                       # luodaan tyhjä tekstikenttä

        self.main_widget = QWidget()                # luodaan pääikkunalle pääwidget
        self.setCentralWidget(self.main_widget)     # asetetaan se pääwidgetiksi

        self.layout = QVBoxLayout()                 # luodaan asettelu
        self.layout.addWidget(self.label)           # lisätään tekstikenttä asetteluun
        self.layout.addWidget(self.button1)         # lisätään nappula asetteluun

        self.main_widget.setLayout(self.layout)     # asetetaan pääwidgetille asettelu

        self.show()                                 # Päivittää ylläolevat määrittelyt näkymään ruudulle

    def show_dialog(self):
        # avataan syote-dialogi, joka pyytää käyttäjältä nimeä
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name')

        # jos dialogin toinen paluuarvo oli True eli käyttäjä painoi ok-nappia
        if ok:
            self.label.setText("{} {}".format('Hello', text))       # aseta tekstikenttään teksti

    # def show_dialog(self):
    #     item, ok = QInputDialog.getItem(self, "Input dialog", "list of names", ["Roosa", "Daniel", "Olli", "Johanna", "Veera", "Ella", "Otto"], 0, False)
    #
    #     if ok and item:
    #         self.label.setText("{} {}".format('Hello', item))

if __name__ == '__main__':
    app = QApplication(sys.argv)                # Luodaan QApplication-olio
    example = Example_mainwindow()
    sys.exit(app.exec())                        # app.exec() aloittaa tapahtumankäsittelyn