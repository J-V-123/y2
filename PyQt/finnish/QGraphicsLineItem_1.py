from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen
from spiral_calculator import calculate_coordinates
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()           # luodaan grafiikka-alue
        self.view = QGraphicsView(self.scene)   # luodaan näkymä, johon grafiikka-alue asetetaan
        self.view.scale(0.5, 0.5)               # skaalataan näkymä 0.5-kertaiseksi
        self.setCentralWidget(self.view)        # asetetaan näkymä Windowin keskiwidgetiksi
        # parameters for the calculator are: (length of the first line, amount of iterations or lines, ratio of the lines)
        self.data = calculate_coordinates(1000, 15, 1.618)        # lasketaan uudet koordinaatit
        self.showMaximized()                                      # näytetään ikkuna

    def paintEvent(self, event):
        for i in self.data:
            line = QGraphicsLineItem(i[0], i[1], i[2], i[3])    # luodaan uusi viiva
            pen = QPen()                                        # luodaan uusi kynä
            pen.setWidthF(0.5)                                  # määritellään kynän leveys
            line.setPen(pen)                                    # määritetään viivan piirtyvän pen:iin asetetuilla määrityksillä
            self.scene.addItem(line)                            # lisätään viiva grafiikka-alueseen

    def mousePressEvent(self, event):                           # uudelleenmääritellään mousePressEvent()-metodi
        if event.button() == Qt.MouseButton.LeftButton:         # jos käyttäjä klikkaa hiiren vasemmalla näppäimellä
            self.view.scale(1.2, 1.2)                           # skaalataan näkymä 1.2-kertaiseksi
        elif event.button() == Qt.MouseButton.RightButton:      # jos käyttäjä klikkaa hiiren oikealla näppäimellä
            self.view.scale(0.5, 0.5)                           # skaalataan näkymä 0.5-kertaiseksi

if __name__ == '__main__':
    app = QApplication(sys.argv)    # luodaan QApplication-olio
    window = Window()               # luodaan Window-olio
    sys.exit(app.exec())            # jäädään odottamaan sovelluksen sulkeutumista