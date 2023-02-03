import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt6.QtGui import QPolygonF, QBrush, QColor, QPen
from PyQt6.QtCore import QPointF, Qt


class PacMan(QGraphicsEllipseItem):                     # peritään ellipsien piirtoon tarkoitettu luokka

    def __init__(self, width, r, g, b):                 # parametreina ympyrän halkaisija, sekä rgb-värin kolme komponenttia
        super().__init__()

        # annetaan ellipsille sitä vastaavan suorakaiteen vasemman yläkulman sijainti sekä leveys ja pituus
        self.setRect(1, 1, width, width)
        self.x = 0                                      # asetetaan x-suuntaisen sijainnin säilyttävä muuttuja nollaksi
        self.setStartAngle(45 * 16)                     # asetetaan aloituskulma
        self.setSpanAngle(270 * 16)                     # asetetaan pyörähdyskulma
        self.setPen(QPen(Qt.GlobalColor.black, 3))      # asetetaan kynä värillä musta ja leveydellä 3 ulkoreunoja varten
        self.setBrush(QColor(r, g, b))                  # maalataan parametrina saadulla värillä pacmanin sisäosa
        self.mouth_open = False                         # tallennetaan suun asento

    def mousePressEvent(self, event):                   # uudelleen määritetään yläluokan metodi mousePressEvent
        if self.mouth_open == False:                    # jos grafiikka-olion suu on kiinni
            self.setStartAngle(25 * 16)                 # muutetaan ellipsin aloituskulmaa
            self.setSpanAngle(335 * 16)                 # ja pyörähdyskulmaa
            self.change_pos()                           # kutsutaan sijaintia muuttavaa metodia
            self.mouth_open = True                      # tallennetaan suun olevan auki
        else:
            self.setStartAngle(45 * 16)
            self.setSpanAngle(270 * 16)
            self.change_pos()
            self.mouth_open = False

    def change_pos(self):
        self.setX(self.x)           # muutetaan grafiikka-olion x-koordinaatiksi x
        self.x += 30                # kasvatetaan x:n arvoa


class Window(QGraphicsView):        # grafiikkaolioille pääikkunana voi käyttää myös näkymää, peritään QGraphicsView

    def __init__(self):
        super(Window, self).__init__()
        self.scene = QGraphicsScene(self)           # luodaan grafiikka-alue
        self.pacman1 = PacMan(150, 102, 255, 178)   # luodaan PacMan-luokasta olio
        self.pacman2 = PacMan(80, 255, 0, 255)      # ja toinen olio
        self.scene.addItem(self.pacman1)            # lisätään ne grafiikka-alueeseen
        self.scene.addItem(self.pacman2)
        self.scene.setSceneRect(0, 0, 300, 300)     # asetetaan grafiikka-alueelle koko
        self.setScene(self.scene)                   # asetetaan näkymälle grafiikka-alue
        self.show()                                 # näytetään ikkunan sisältö


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Window()                               # luodaan ikkuna
    sys.exit(app.exec())