from PyQt6.QtWidgets import QGraphicsEllipseItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QColor

from item_graphics import ItemGraphics


class CircleGraphicsItem(QGraphicsEllipseItem):
    """
    This class handles drawing of the circles and their functions.
    """

    def __init__(self, x, y, game):
        super().__init__()

        self.rectsize = 70  # Length of the side of a square that can surround the circle

        self.x = 15 + x * 100  # Adjusting the circle's position
        self.y = 15 + y * 100

        self.setRect(self.x, self.y, self.rectsize, self.rectsize)
        self.setPen(QPen(Qt.GlobalColor.black, 3))
        self.setBrush(QColor(0, 175, 255))

        self.isEmpty = True
        self.item = None

        self.game = game

    def mousePressEvent(self, *args, **kwargs):
        """
        If the circle is clicked, the method adds an item to the circle.
        This method is called every time this object is clicked on the scene.

        Hint: You don't need to do anything with the *args or **kwargs. A one line solution should be sufficient.
        """
        # http://doc.qt.io/qt-6/qgraphicsitem.html#mousePressEvent

        if self.isEmpty:
            # Call an appropriate method to add an item to the circle (Hint: from Game-class)
            self.game.add_item_to_circle(self)
