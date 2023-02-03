from PyQt6.QtWidgets import QGraphicsPolygonItem
from PyQt6.QtGui import QPolygonF, QColor, QTransform
from PyQt6.QtCore import QPointF

WIDTH, HEIGHT = 80, 40

class Player(QGraphicsPolygonItem):
    def __init__(self):
        super().__init__()
        self.init_player()

    def init_player(self):
        # asetetaan maksiminopeudeksi 8, ja nykyiseksi nopeudeksi 0
        self.max_speed_x, self.speed = 8, 0
        # asetetaan, että pelaaja ei liiku kumpaankaan suuntaan aluksi
        self.moving_right, self.moving_left = False, False

        self.setBrush(QColor(255, 192, 203))    # asetetaan pelaajan väri

        self.polygon = QPolygonF()              # luodaan QPolygonF()-olio

        self.polygon.append(QPointF(0, 0))      # polygonin muoto tehdään yhdistelemällä pisteitä toisiinsa
        self.polygon.append(QPointF(0, HEIGHT))
        self.polygon.append(QPointF(WIDTH, HEIGHT))
        self.polygon.append(QPointF(WIDTH, HEIGHT * 0.4))
        self.polygon.append(QPointF(WIDTH * 0.8, HEIGHT * 0.4))
        self.polygon.append(QPointF(WIDTH * 0.6, 0))
        self.polygon.append(QPointF(0, 0))

        self.setPolygon(self.polygon)       # asetetaan luoto polygoni pelaajan muodoksi

    def update_velocities(self):            # metodi, jossa päivitetään pelaajan nopeuksia
        if self.moving_right:
            self.speed = self.max_speed_x
            self.setTransform(QTransform().scale(1, 1))     # käännettään pelaaja alkuperäiseen asentoon
        if self.moving_left:
            self.speed = -self.max_speed_x
            self.setTransform(QTransform().scale(-1, 1))    # käännetään pelaaja peilattuun asentoon

    def update_position(self):              # metodi, jossa liikutetaan pelaajaa
        self.moveBy(self.speed, 0)          # liikutetaan pelaajaa x-akselilla self.speedin verran, y-akselilla 0
