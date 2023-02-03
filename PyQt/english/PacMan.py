import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt6.QtGui import QPolygonF, QBrush, QColor, QPen
from PyQt6.QtCore import QPointF, Qt


class PacMan(QGraphicsEllipseItem):        # the class intended for drawing ellipses is inherited

    def __init__(self, width, r, g, b):    # parameters are the diameter of the circle and the three components of the rgb color
        super().__init__()

        # gives the ellipse the position of the upper left corner of the corresponding rectangle, as well as the width and length
        self.setRect(1, 1, width, width)
        self.x = 0                                      # sets the x-position holding variable to zero
        self.setStartAngle(45 * 16)                     # the start angle is set
        self.setSpanAngle(270 * 16)                     # the rotation angle is set
        self.setPen(QPen(Qt.GlobalColor.black, 3))      # set a pen with color black and width 3 for the outer edges
        self.setBrush(QColor(r, g, b))                  # the inner part of pacman is painted with the color obtained as a parameter
        self.mouth_open = False                         # the position of the mouth is set


    def mousePressEvent(self, event):                   # redefine the mousePressEvent method of the parent class
        if self.mouth_open == False:                    # if the graphic object's mouth is closed
            self.setStartAngle(25 * 16)                 # the starting angle of the ellipse is changed
            self.setSpanAngle(335 * 16)                 # and rotation angle
            self.change_pos()                           # is called the location-changing method
            self.mouth_open = True                      # set the mouth open
        else:
            self.setStartAngle(45 * 16)
            self.setSpanAngle(270 * 16)
            self.change_pos()
            self.mouth_open = False

    def change_pos(self):
        self.setX(self.x)           # is changed to the x-coordinate of the graphic object x
        self.x += 30                # increasing the value of x


class Window(QGraphicsView):        # for graphics objects, you can also use a view as a window, QGraphicsView is inherited

    def __init__(self):
        super(Window, self).__init__()
        self.scene = QGraphicsScene(self)           # a graphics area is created
        self.pacman1 = PacMan(150, 102, 255, 178)   # an object is created from the PacMan class
        self.pacman2 = PacMan(80, 255, 0, 255)      
        self.scene.addItem(self.pacman1)            # add them to the graphics area
        self.scene.addItem(self.pacman2)
        self.scene.setSceneRect(0, 0, 300, 300)     # set to the size of the graphics area
        self.setScene(self.scene)                   # set the graphics area to the view
        self.show()                                 # the contents of the window are displayed


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = Window()                               # a window is created
    sys.exit(app.exec())