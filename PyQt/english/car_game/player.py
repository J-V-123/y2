from PyQt6.QtWidgets import QGraphicsPolygonItem
from PyQt6.QtGui import QPolygonF, QColor, QTransform
from PyQt6.QtCore import QPointF

WIDTH, HEIGHT = 80, 40

class Player(QGraphicsPolygonItem):
    def __init__(self):
        super().__init__()
        self.init_player()

    def init_player(self):
        # set the maximum speed to 8, and the current speed to 0
        self.max_speed_x, self.speed = 8, 0
        # it is set that the player does not move in either direction initially
        self.moving_right, self.moving_left = False, False

        self.setBrush(QColor(255, 192, 203))    # the player's color is set

        self.polygon = QPolygonF()              # a QPolygonF() object is created

        self.polygon.append(QPointF(0, 0))      # the shape of a polygon is made by connecting points together
        self.polygon.append(QPointF(0, HEIGHT))
        self.polygon.append(QPointF(WIDTH, HEIGHT))
        self.polygon.append(QPointF(WIDTH, HEIGHT * 0.4))
        self.polygon.append(QPointF(WIDTH * 0.8, HEIGHT * 0.4))
        self.polygon.append(QPointF(WIDTH * 0.6, 0))
        self.polygon.append(QPointF(0, 0))

        self.setPolygon(self.polygon)       # sets the created polygon as the player's shape

    def update_velocities(self):            # method to update the player's speeds
        if self.moving_right:
            self.speed = self.max_speed_x
            self.setTransform(QTransform().scale(1, 1))     # turn the player to the original position
        if self.moving_left:
            self.speed = -self.max_speed_x
            self.setTransform(QTransform().scale(-1, 1))    # turn the player into a mirrored position

    def update_position(self):          # method of moving the player
        self.moveBy(self.speed, 0)      # move the player on the x-axis by self.speed, on the y-axis 0