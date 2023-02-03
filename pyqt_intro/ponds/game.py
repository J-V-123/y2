from circle_graphics_item import CircleGraphicsItem
from item_graphics import ItemGraphics


class Game():
    """
    This class handles the game's main functionality.
    """

    def __init__(self, scene):
        self.scene = scene  # QGraphicsScene is passed from the MainWindow so graphical objects can be added from the Game-class

        self.circles = []
        self.init_circles()

        self.item_to_add = 0  # 0 for fish, 1 for bucket, 2 for boot

    def init_circles(self):
        """
        Adds the circles to the scene.
        """

        for y in range(3):
            for x in range(3):
                circle = CircleGraphicsItem(x, y, self)
                self.scene.addItem(circle)
                self.circles.append(circle)  # Add circles to the list for testing the exercise

    def switch_item_type(self, type):
        """
        Switches the type of an item to be next added to the scene.
        """

        self.item_to_add = type

    def add_item_to_circle(self, circle):
        """
        Creates a new item and adds it to the middle of the circle.
        """

        item = ItemGraphics(self.item_to_add)
        circle.item = item

        circle_x = circle.x
        circle_y = circle.y

        self.scene.addItem(item)
        item.setPos(circle_x + 5, circle_y + 5)

        circle.isEmpty = False

    def remove_item_from_circle(self, circle):
        """
        Removes an item from the circle.
        """

        self.scene.removeItem(circle.item)
        circle.item = None
        circle.isEmpty = True

    def clear_items(self):
        """
        Removes all items from the circles.
        """

        for circle in self.circles:
            self.remove_item_from_circle(circle)
