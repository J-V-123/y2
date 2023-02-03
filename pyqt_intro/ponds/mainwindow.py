from PyQt6 import QtWidgets
from game import Game


class MainWindow(QtWidgets.QMainWindow):
    """
    This class handles interaction and drawing of the game.
    """

    def __init__(self):
        super().__init__()

        """
        TODO:
            - Create the layouts and set the correct layout as the central widget
        """
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QHBoxLayout()
        self.vertical = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.vertical)

        self.setCentralWidget(self.main_widget)  # QMainWindow must have a centralWidget to be able to add layouts
        self.main_widget.setLayout(self.main_layout)

        self.init_window()

        self.game = Game(self.scene)

        self.init_buttons()

    def init_buttons(self):
        """
        Adds buttons to the window and connects them to their respective functions
        See: QPushButton at https://doc.qt.io/qt-6/qpushbutton.html

        """

        self.fish_button = QtWidgets.QPushButton("Fish")
        self.fish_button.clicked.connect(lambda: self.game.switch_item_type(0))
        self.vertical.insertWidget(0, self.fish_button)

        self.bucket_button = QtWidgets.QPushButton("Bucket")
        self.bucket_button.clicked.connect(lambda: self.game.switch_item_type(1))
        self.vertical.insertWidget(1, self.bucket_button)

        self.boot_button = QtWidgets.QPushButton("Boot")
        self.boot_button.clicked.connect(lambda: self.game.switch_item_type(2))
        self.vertical.insertWidget(2, self.boot_button)

        self.clear_button = QtWidgets.QPushButton("Clear")
        self.clear_button.clicked.connect(self.game.clear_items)
        self.vertical.insertWidget(3, self.clear_button)

    def init_window(self):

        self.setWindowTitle("Ponds")
        self.setGeometry(500, 400, 450, 350)

        self.show()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)  # Setting the size of the scene

        self.view = QtWidgets.QGraphicsView()  # Creating a QGraphicsView-widget where the QGraphicsScene will be added
        self.view.setScene(self.scene)  # Adding the scene to the QGraphicsView
        self.view.show()
        self.main_layout.addWidget(self.view)
