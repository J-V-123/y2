import sys
from PyQt6 import QtWidgets
from counter import Counter


class MainWindow(QtWidgets.QMainWindow):
    """
    This class handles interaction and drawing of the window.  
    """

    def __init__(self):
        super().__init__()

        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QHBoxLayout()
        self.vertical = QtWidgets.QVBoxLayout()

        self.main_layout.addLayout(self.vertical)

        self.setCentralWidget(self.main_widget)  # QMainWindow must have a centralWidget to be able to add layouts
        self.main_widget.setLayout(self.main_layout)  # Setting the layout

        self.init_window()

        self.counter = Counter()
        self.scene.addItem(self.counter)

        self.init_button()

    def init_button(self):
        """
        Adds the button to the window and connects it to it's respective function
        See: QPushButton at https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QPushButton.html
        """

        self.counter_button = QtWidgets.QPushButton("Add +1")
        self.counter_button.clicked.connect(self.counter.add)
        self.reset_button = QtWidgets.QPushButton("Reset")
        self.reset_button.clicked.connect(self.counter.reset)

        self.vertical.insertWidget(0, self.counter_button)
        self.vertical.insertWidget(1, self.reset_button)

    def init_window(self):
        """
        Sets up the window.
        """

        self.setWindowTitle('Counter')
        self.setGeometry(500, 400, 500, 350)  # Setting the size of the main window
        self.show()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 100, 100)  # Setting the size of the scene

        self.view = QtWidgets.QGraphicsView()  # Creating a QGraphicsView-widget where the QGraphicsScene will be added
        self.view.setScene(self.scene)

        self.view.show()

        self.main_layout.addWidget(self.view)  # The QGraphicsView-widget is added to the horizontal layout


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Launch an instance of QApplication
    window = MainWindow()
    sys.exit(app.exec())  # Start the Qt event loop
