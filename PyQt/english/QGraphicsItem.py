from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QApplication, \
    QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsPolygonItem, QGraphicsPixmapItem
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QColor, QPolygonF, QPixmap
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()  # creating a scene
        self.view = QGraphicsView(self.scene)  # creating a view and giving the scene to it as a parameter
        self.setCentralWidget(self.view)  # setting the view to the central widget
        self.setGeometry(0, 0, 400, 800)
        self.show()

    def paintEvent(self, event):  # overwriting the paintEvent method of the base class

        # draw two rectangles

        rec_1 = QGraphicsRectItem(2, 2, 90,
                                  40)  # creating a graphics item, and giving following parameters: location of the top left corner, width and lenght
        rec_1.setBrush(QColor(178, 255, 102))  # coloring the graphics item
        self.scene.addItem(rec_1)  # adding the item to the scene

        rec_2 = QGraphicsRectItem(90, 2, 90, 40)
        rec_2.setBrush(QColor(255, 204, 255))
        self.scene.addItem(rec_2)

        # draw half circle
        circle = QGraphicsEllipseItem(2, 60, 100,
                                      100)  # creating an ellipse, and giving the following parameters: location of the top left corner of the retangle corresponding to the ellipse and the width and length of it
        circle.setStartAngle(180 * 16)  # as we don't want the whole circle, we set a start angle
        circle.setSpanAngle(180 * 16)  # and a span angle. Now it spans 180 to anti clock wise. 1 degree is 16 units
        circle.setBrush(QColor(0, 102, 51))
        self.scene.addItem(circle)

        # draw line

        line = QGraphicsLineItem(2, 200, 150, 200)  # creating a line item from point (2, 200) to (150, 200)
        pen = QPen()  # creating a pen
        pen.setWidthF(3)  # setting a width to it
        line.setPen(pen)  # setting the pen to the line
        self.scene.addItem(line)  # adding the line to the scene

        # draw polygon

        polygon = QPolygonF([QPointF(2, 250), QPointF(100, 250), QPointF(100, 400), QPointF(51, 450),
                             QPointF(2, 400)])  # creating a QPolygonF object with a list of QPointF -objects
        pol_item = QGraphicsPolygonItem(polygon)  # creating the graphics polygon item
        pol_item.setBrush(QColor(153, 204, 255))  # coloring it
        self.scene.addItem(pol_item)  # adding the polygon item to the scene

        # dwaw pixmap item

        pixmap = QPixmap('image.png')  # creating a pixmap object for the picture
        pixmap = pixmap.scaledToHeight(200)  # scaling the pixmap to a reasonable size
        pixmap_item = QGraphicsPixmapItem(pixmap)  # greating a graphical picture object
        pixmap_item.setPos(2, 500)  # changing the location of it
        self.scene.addItem(pixmap_item)  # adding it to the scene


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
