from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QApplication, \
        QPushButton, QLabel, QVBoxLayout, QWidget, QSlider
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QCloseEvent, QGuiApplication
from spiral_calculator import calculate_coordinates
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()                 # a vertical layout is created for the window
        self.setLayout(self.layout)                 # sets the created layout as the layout of this window

        self.scene = QGraphicsScene()               # a graphics area is created
        self.view = QGraphicsView(self.scene)       # a view is created in which the graphics area is placed
        self.layout.addWidget(self.view)            # a view is added to the layout

        self.data = []                              # initialize self.data as an empty list
        self.view.scale(0.5, 0.5)                   # scale the view a bit further to ensure that
                                                    # when the window opens, the view shows the entire line spiral

    def paintEvent(self, event):                    # implementations of the methods are the same as in the previous example
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Adjust the ratio")         # a text field is created
        self.button = QPushButton("Create a figure")    # button is created
        self.slider = QSlider()                         # slider is created
        self.slider.setMinimum(1)                       # set the slider min value
        self.slider.setMaximum(600)                     # set the slider max value

        self.layout = QVBoxLayout()                     # create vertical layout
        self.layout.addWidget(self.label)               # add textlabel to the layout
        self.layout.addWidget(self.slider)              # add slider to layout
        self.layout.addWidget(self.button)              # add button to layout

        self.central_widget = QWidget()                 # create new QWdiget
        self.central_widget.setLayout(self.layout)      # sets the previously created self.layout as its layout
        self.setCentralWidget(self.central_widget)      # let's set it as MainWindow's main widget

        self.button.clicked.connect(self.show_figure)   # connect the signal from pressing the button to the show_figure method
        self.showMaximized()                            # display on the screen

    def show_figure(self):
        self.window = Window()                                      # create new window
        converted_value = 1 + float(self.slider.value() * 0.001)    # adjust the values of the sliders
        self.window.data = calculate_coordinates(1000, 15, converted_value)     # calcuate new coordinates based on new values

            # sets the opening window to be 70% of the remaining space
        self.window.resize(QGuiApplication.primaryScreen().availableGeometry().size() * 0.7)   
        self.window.show()      # show window

    def closeEvent(self, a0: QCloseEvent):
        if self.window:             # closes the opened window if the main window is closed
            self.window.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)   
    main_window = MainWindow()      
    sys.exit(app.exec())   