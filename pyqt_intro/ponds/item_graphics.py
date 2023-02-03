from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap


class ItemGraphics(QGraphicsPixmapItem):
    """
    This class handles drawing of the items.
    """

    def __init__(self, type):

        super().__init__()

        self.type = type  # Determines which type of item is drawn

        self.set_image()

    def set_image(self):
        """
        Sets the correct Pixmap-image depending on the type.
        """

        if self.type == 0:
            self.setPixmap(QPixmap('fish.png'))

        elif self.type == 1:
            self.setPixmap(QPixmap('bucket.png'))

        elif self.type == 2:
            self.setPixmap(QPixmap('boot.png'))

    def location(self):
        """
        Returns the item's location on the scene
        """

        return self.x(), self.y()
