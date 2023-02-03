from PyQt6.QtWidgets import QGraphicsTextItem


class Counter(QGraphicsTextItem):
    """
    This class handles the functionality and drawing of the counter.
    """

    def __init__(self):
        super().__init__()
        self.count = 0
        self.setPlainText('Count: 0')

        font = self.font()
        font.setPointSize(15)  # Font size
        font.setWeight(4500)  # Font thickness
        self.setFont(font)

        self.setPos(0, 30)  # Adjusting the position

    def add(self):
        """
        Adds 1 to the counter every time the function is called
        and draws the correct value to it's graphical object.
        """

        self.count += 1
        self.setPlainText('Count: {}'.format(self.count))

    def reset(self):
        self.count = 0
        self.setPlainText("Count: 0")
