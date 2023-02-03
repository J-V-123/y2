import sys
from PyQt6.QtCore import QPointF, QRectF, Qt
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtWidgets import (QApplication, QGraphicsItem, QGraphicsScene,
                         QGraphicsView, QMainWindow)


class RistiNolla(QGraphicsItem):            # peritään QGraphicsItem-luokka

    def __init__(self):
        super(RistiNolla, self).__init__()
        self.lauta = [[None, None, None], [None, None, None], [None, None, None]]  # luodaan kaksiulotteinen lista laudalle
        self.Nolla = 0
        self.Risti = 1
        self.vuoro = self.Nolla

    def boundingRect(self):         # määritetään uudelleen yläluokan metodi, joka asettaa grafiikka-olion piirtoalueen rajat
        return QRectF(0, 0, 300, 300)           # rajoiksi asetetaan neliö

    def select(self, x, y):
        if x < 0 or y < 0 or x >= 3 or y >= 3:
            return
        if self.lauta[y][x] == None:            # jos klikattua ruutua vastaava ruutu on tyhjä
            self.lauta[y][x] = self.vuoro       # lisätään sen merkki, jonka vuoro on
            self.vuoro = 1 - self.vuoro         # vaihdetaan vuoro seuraavalle

    def paint(self, painter, option, widget):        # uudelleen määritetään yläluokan paint() -metodi
        painter.setPen(Qt.GlobalColor.black)         # asetetaan painter:ille kynä, jonka väri on musta

        # piirretään ruudukon viivat (siis joka kerta uudestaan kun metodia kutsutaan)
        painter.drawLine(0, 100, 300, 100)          # piirretään viiva pisteestä (0, 100) pisteeseeen (300, 100) jne
        painter.drawLine(0, 200, 300, 200)
        painter.drawLine(100, 0, 100, 300)
        painter.drawLine(200, 0, 200, 300)
        for y in range(3):                          # käydään for-loopilla laudan (kaksiulotteisen listan) ruudut läpi
            for x in range(3):
                if self.lauta[y][x] == self.Nolla:  # jos ruudussa on 0

                    # asetetaan kynä, jonka väri on punainen ja leveys 3
                    painter.setPen(QPen(Qt.GlobalColor.red, 3))
                    painter.drawEllipse(QPointF(50+x*100, 50+y*100), 35, 35)       # ja piirretään ellipsi
                elif self.lauta[y][x] == self.Risti:                               # jos ruudussa on X
                    painter.setPen(QPen(Qt.GlobalColor.blue, 3))                   # asetetaan  sininen kynä
                    painter.drawLine(20+x*100, 20+y*100, 80+x*100, 80+y*100)       # ja piirretään rastin viiva
                    painter.drawLine(20+x*100, 80+y*100, 80+x*100, 20+y*100)       # ja toinen viiva

    # määritetään yläluokan metodi uudestaan, tämä ajetaan kun hiirellä painetaan näyttöä
    def mousePressEvent(self, event):

        # hiirenpainnallustapahtuman sijainneista lasketaan oikea ruutu, ja kutsutaan select() -metodia
        self.select(int(event.pos().x()/100), int(event.pos().y()/100))

        # päivitetään näyttö, mikä aikaansaa paint() -metodin kutsumisen
        self.update()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        scene = QGraphicsScene()                # luodaan grafiikka-alue
        view = QGraphicsView(scene)             # luodaan näkymä, ja asetetaan sille grafiikka-alue
        self.setCentralWidget(view)             # asetetaan näkymä pääwidgetiksi
        self.setGeometry(0, 0, 320, 320)        # asetetaan ikkunan koko
        self.ristinolla = RistiNolla()          # luodaan peli
        scene.addItem(self.ristinolla)          # lisätään luotu grafiikka-komponentti grafiikka-alueeseen
        self.show()                             # näytetään määrittelyt ruudulle


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())