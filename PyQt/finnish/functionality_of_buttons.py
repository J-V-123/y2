import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QRadioButton, QLabel
from PyQt6.QtGui import QPixmap

class Example_window(QWidget):

    def __init__(self):

        super().__init__()
        self.setGeometry(20, 20, 700, 350)                      # asetetaan ikkunalle koko

        self.radiobutton1 = QRadioButton('Show picture', self)  # luodaan valinta-nappula
        self.radiobutton2 = QRadioButton('Hide picture', self)  # luodaan valinta-nappula
        self.button = QPushButton('Change to blue', self)       # luodaaan paino-nappula
        self.checkbox = QCheckBox('Use custom title', self)     # luodaan rastitusruutu

        self.radiobutton2.move(0, 30)                           # siirretään nappuloita
        self.button.move(0, 80)
        self.checkbox.move(0, 140)

        self.show()                 # Päivittää ylläolevat määrittelyt näkymään ruudulle

        # yhdistetään paino-nappulan klikkaus määrittämäämme metodiin button_clicked()
        self.button.clicked.connect(self.button_clicked)

        # yhdistään rastitusruudun tilan muutos määrittämäämme metodiin checkbox_clicked()
        self.checkbox.stateChanged.connect(self.checkbox_clicked)

        # yhdistetään valinta-nappulan klikkaus määrittämäämme metodiin radio_button_clicked()
        self.radiobutton1.clicked.connect(self.radio_button_clicked)
        self.radiobutton2.clicked.connect(self.radio_button_clicked)

        # luodaan kuva. Huomaa, että tämä on self.show():n jälkeen, joten kuva ei näy näytöllä.
        self.picture = QPixmap("image.png")

        # Muutetaan kokoa. ScaledToHeight palauttaa skaalatun kuvan, joka tallennetaan muuttujaan
        self.picture = self.picture.scaledToHeight(300)
        self.label_picture = QLabel(self)                       # luodaan kuvalle kenttä
        self.label_picture.move(300, 20)                        # siirretään kentän sijaintia
        self.label_picture.setPixmap(self.picture)              # asetetaan kuva kenttään

    def button_clicked(self):
        if self.button.text() == "Change to blue":                  # katsotaan onko painonappulan teksti tämä
            self.button.setStyleSheet("background-color : blue;")   # muutetaan painonappulan väriä
            self.button.setText("Change to red")                    # asetetaan painonappulalle uusi teksti
        else:
            self.button.setStyleSheet("background-color : red;")
            self.button.setText("Change to blue")

    def checkbox_clicked(self, state):
        if self.checkbox.isChecked():               # katsotaan onko rastitusruudun ruutu rastitettu vai ei
            self.setWindowTitle('My own title')
        else:
            self.setWindowTitle('')

    def radio_button_clicked(self):
        if self.radiobutton1.isChecked():       # katsotaan onko valintanapeista valittu nappula 1 vai nappula 2
            self.label_picture.show()           # näytetään QLabel näytölle
        else:
            self.label_picture.hide()           # piilotetaan QLabel

if __name__ == '__main__':
    app = QApplication(sys.argv)                # Luodaan QApplication-olio
    example = Example_window()
    sys.exit(app.exec())