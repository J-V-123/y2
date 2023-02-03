from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen
from spiral_calculator import calculate_coordinates
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()           # creating a scene
        self.view = QGraphicsView(self.scene)   # creating a view and giving the scene to it as a parameter
        self.view.scale(0.5, 0.5)               # zooming the view with the scaling factor of 0.5
        self.setCentralWidget(self.view)        # setting the view to be the central widget
        # parameters for the calculator are: (length of the first line, amount of iterations, ratio (1.618 is the golden ratio))
        self.data = calculate_coordinates(1000, 15, 1.618)        # calculating new coordinates
        self.showMaximized()                                                # diplaying the window

    def paintEvent(self, event):
        for i in self.data:
            line = QGraphicsLineItem(i[0], i[1], i[2], i[3])    # creating a new line
            pen = QPen()                                        # creating a new pen
            pen.setWidthF(0.5)                                  # setting a width for the pen
            line.setPen(pen)                                    # setting the pen to the line
            self.scene.addItem(line)                            # adding the line to the scene

    def mousePressEvent(self, event):                           # overwriting the mousePressEvent()-method
        if event.button() == Qt.MouseButton.LeftButton:         # if the user clicks with the left button of the mouse
            self.view.scale(1.2, 1.2)                           # the view is scaled with the scaling factor of 1.2
        elif event.button() == Qt.MouseButton.RightButton:      # if the user clicks with the right button of the mouse
            self.view.scale(0.5, 0.5)                           # the view is scaled with the scaling factor of 0.5

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

main()