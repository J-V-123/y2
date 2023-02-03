import sys
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QApplication


class Example_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 300, 200)  # määritetään ikkunan sijainti ja koko

        self.qLabel = QLabel(self)  # luodaan tesktikenttä
        self.qLineEdit = QLineEdit(self)  # luodaan tekstieditori
        self.qLineEdit.move(70, 50)  # siirretään tesktieditoria
        self.qLabel.move(70, 120)  # siirretään tesktikenttää

        # yhdistetään editorin tekstin muuttuminen onChanged() -metodin ajamiseen
        self.qLineEdit.textChanged[str].connect(self.onChanged)
        self.show()

    def onChanged(self, text):
        self.qLabel.setText(text)  # asetetaan tekstikenttään parametrina annettu teksti
        self.qLabel.adjustSize()  # vaihdetaan kentän koko vastaavaan siinä olevan tekstin kokoa


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example_Window()
    sys.exit(app.exec())
