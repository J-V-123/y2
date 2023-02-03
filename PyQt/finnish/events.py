import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 100)        # asetetaan ikkunalle koko
        self.label = QLabel(self)               # luodaan tyhjä tekstikenttä

        # asetetaan sille taustaväri, merkkijonon teksti on CSS-kieltä
        self.label.setStyleSheet("background-color : pink;")
        self.show()                             # näytetään määrittelyt näytölle

    # Uudelleenmääritetään QWidgetin keyPressEvent()-metodi, jotta voimme reagoida näppäimistön painalluksiin
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_T:     # jos parametrina saadun tapahtuma-olion näppäin on T
            self.label.setText("You pressed the key T") # muutetaan tekstikenttään teksti
        elif event.key() == Qt.Key.Key_Y:
            self.label.setText("You pressed the key Y")
        else:
            self.label.setText("You pressed some key that is not T or Y")
        self.label.adjustSize()             # muutetaan tesktikentän koko vastaaman tekstin pituutta

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())