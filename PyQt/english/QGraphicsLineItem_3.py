from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsLineItem, QApplication, \
    QLabel, QVBoxLayout, QWidget, QSlider, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QColor
from spiral_calculator import calculate_coordinates
import sys


class Figure(QGraphicsScene):
    def __init__(self, view, ratio, lines, width):
        super().__init__()
        self.data = []  # initialize self.data as an empty list
        self.pen_width = width  # set self.pen_width to be the width
        self.view = view  # sets self.view to be view
        self.ratio = ratio  # set self.view to be ratio
        self.data = calculate_coordinates(1000, lines, ratio)  # calculate the coordinates
        self.paint_lines()  # method paint_lines is called, where lines are drawn

    def paint_lines(self):  # Note, this is not a standard method of QGraphicsScene
        for i in self.data:
            line = QGraphicsLineItem(i[0], i[1], i[2], i[3])  # a new line is created
            pen = QPen()  # a new pen is created
            if 1.6 <= self.ratio <= 1.63:  # if we are approximately in the area of the golden section
                pen.setColor(QColor(255, 215, 0))  # let's color the line golden
            pen.setWidthF(self.pen_width)  # defines the width of the pen
            line.setPen(pen)  # specifies that the line is drawn with the specifications set in 'pen'
            self.addItem(line)  # a line is added to the graphics area

    def mousePressEvent(self, event):  # redefining the mousePressEvent() method
        if event.button() == Qt.MouseButton.LeftButton:  # if the user clicks with the left mouse button
            self.view.scale(1.2, 1.2)  # let's scale the view to 1.2 times
        elif event.button() == Qt.MouseButton.RightButton:  # if the user clicks with the right mouse button
            self.view.scale(0.5, 0.5)  # let's scale the view to 0.5 times


class MainWindow(QWidget):  # Note: MainWindow now does not inherit the class QMainWindow but the class QWidget
    def __init__(self):
        super().__init__()

        self.ratio_slider = QSlider(Qt.Orientation.Horizontal)  # create a horizontal slider
        self.ratio_slider.setMinimum(1)  # set the slider min value
        self.ratio_slider.setMaximum(2000)  # set the slider max value
        self.ratio_slider.setValue(300)  # set the slider current value 300

        self.line_slider = QSlider(Qt.Orientation.Horizontal)  # repeat same as above
        self.line_slider.setMinimum(5)
        self.line_slider.setMaximum(500)

        self.pen_slider = QSlider(Qt.Orientation.Horizontal)
        self.pen_slider.setMinimum(1)
        self.pen_slider.setMaximum(20)
        self.pen_slider.setValue(10)

        self.container = QVBoxLayout()  # create vertical layout

        self.ratio_label = QLabel()  # create QLabel objects for the values of the sliders
        self.line_label = QLabel()
        self.pen_label = QLabel()

        self.calculate_and_set_values()  # use method self.calculate_and_set_values()

        self.ratio_container = QHBoxLayout()  # create horizontal layout for the ratio
        self.ratio_container.addWidget(QLabel("Adjust the ratio"))  # add QLabel to the layout
        self.ratio_container.addWidget(self.ratio_slider)  # adds a slider to the layout
        self.ratio_container.addWidget(
            self.ratio_label)  # a self.ratio_label is added to show the value of the current ratio

        self.line_container = QHBoxLayout()  # repeat the same as above, but now for lines
        self.line_container.addWidget(QLabel("Adjust the amount of lines"))
        self.line_container.addWidget(self.line_slider)
        self.line_container.addWidget(self.line_label)

        self.pen_container = QHBoxLayout()
        self.pen_container.addWidget(QLabel("Adjust the width of line"))
        self.pen_container.addWidget(self.pen_slider)
        self.pen_container.addWidget(self.pen_label)

        self.view = QGraphicsView()  # a new view is created
        self.view.scale(0.7, 0.7)  # let's scale the view to 0.7 times
        self.figure = Figure(self.view, self.ratio_value, self.line_value, self.pen_value)  # a new Figure is created
        self.view.setScene(self.figure)  # set to Figure view

        self.container.addLayout(self.ratio_container)  # adding a layout of the ratio to self.container layout
        self.container.addLayout(self.line_container)  # adding a line layout to the self.container layout
        self.container.addLayout(self.pen_container)  # add pen layout to self.container layout
        self.container.addWidget(self.view)  # the view itself is added to the self.container layout

        self.setLayout(self.container)  # sets self.container as the layout of this window

        self.ratio_slider.valueChanged.connect(
            self.update_figure)  # combine the signals if the values of the sliders change
        self.line_slider.valueChanged.connect(self.update_figure)
        self.pen_slider.valueChanged.connect(self.update_figure)
        self.showMaximized()  # displays the screen

    def update_figure(self):
        self.calculate_and_set_values()  # new values are calculated and set
        self.figure = Figure(self.view, self.ratio_value, self.line_value, self.pen_value)  # a new Figure is created
        self.view.setScene(self.figure)  # add it to the view

    def calculate_and_set_values(
            self):  # in this method, new values are calculated and each one is placed in its own QLabel
        self.ratio_value = 1 + float(self.ratio_slider.value() * 0.001)
        self.line_value = self.line_slider.value()
        self.pen_value = self.pen_slider.value() / 10

        self.ratio_label.setNum(self.ratio_value)
        self.line_label.setNum(self.line_value)
        self.pen_label.setNum(self.pen_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
