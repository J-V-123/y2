from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QApplication, QGraphicsRectItem, \
    QGraphicsEllipseItem, QGraphicsPolygonItem, QGraphicsPixmapItem
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QColor, QPolygonF, QPixmap
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()                           # luodaan scene
        self.view = QGraphicsView(self.scene)                   # luodaan view, ja asetetaan sille scene
        self.setCentralWidget(self.view)                        # asetetaan view pääwidgetiksi
        self.setGeometry(0, 0, 400, 800)
        self.show()


    def paintEvent(self, event):                                # uudelleen määritetään yläluokan paintEvent-metodi

        #piirretään kaksi suorakuolmiota

        # luodaan grafiikkaolio, parametreina vasemman yläkulman sijainti, leveys ja pituus
        rec_1 = QGraphicsRectItem(2, 2, 90, 40)
        rec_1.setBrush(QColor(178, 255, 102))                   # väritetään grafiikka-olio
        self.scene.addItem(rec_1)                               # lisätään grafiikka-olio sceneen

        rec_2 = QGraphicsRectItem(90, 2, 90, 40)
        rec_2.setBrush(QColor(255, 204, 255))
        self.scene.addItem(rec_2)

        #piirretään puoliympyrä

        # luodaan ellipsi, parametrina ellipsiä vastaavan suorakaiteen vasemman yläkulman sijainti, sen leveys sekä pituus
        circle = QGraphicsEllipseItem(2, 60, 100, 100)
        circle.setStartAngle(180 * 16)                          # koska emme halua koko ympyrää, asetamme aloituskulman
        circle.setSpanAngle(180 * 16)                           # ja pyörähdyskulman, eli nyt kiertää 180 astetta
                                                                # aloituskulmasta myötäpäivään. 1 aste on 16 yksikköä
        circle.setBrush(QColor(0, 102, 51))
        self.scene.addItem(circle)

        #piirretään viiva

        line = QGraphicsLineItem(2, 200, 150, 200)              # luodaan viiva pisteestä (2, 200) pisteeseen (150, 200)
        pen = QPen()                                            # luodaan kynä
        pen.setWidthF(3)                                        # asetetaan sille leveys
        line.setPen(pen)                                        # asetetaan viivalle kynä
        self.scene.addItem(line)                                # asetetaan viiva sceneen

        #piirretään polygoni

        # luodaan pisteitä
        points = [QPointF(2,250), QPointF(100,250), QPointF(100, 400), QPointF(51, 450), QPointF(2, 400)]
        polygon = QPolygonF(points)                             # luodaan pisteistä QPolygonF -olio
        pol_item = QGraphicsPolygonItem(polygon)                # luodaan polygonigrafiikka-olio
        pol_item.setBrush(QColor(153, 204, 255))                # maalataan se
        self.scene.addItem(pol_item)

        #piirretään pixmap-olio

        pixmap = QPixmap('image.png')                           # luodaan kuvalle pixmap-olio
        pixmap = pixmap.scaledToHeight(200)                     # muutetaan sen kokoa
        pixmap_item = QGraphicsPixmapItem(pixmap)               # luodaan pixmap-grafiikka-olio ja asetetaan sille pixmap
        pixmap_item.setPos(2, 500)                              # siirretään grafiikka-olion sijaintia
        self.scene.addItem(pixmap_item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())