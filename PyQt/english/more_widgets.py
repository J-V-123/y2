import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QDial, QComboBox, QCalendarWidget, QSpinBox, QTabWidget, QScrollArea, QLabel, QProgressBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from QGraphicsItem import Window


class Example_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("some widgets that might be useful")
        self.layout = QVBoxLayout()

        #Slider
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(600)
        self.layout.addWidget(self.slider)

        #ComboBox
        self.box = QComboBox()
        self.box.addItems(["apples","bananas", "oranges", "grapes"])
        self.layout.addWidget(self.box)

        #Dial
        self.dial = QDial()
        self.layout.addWidget(self.dial)

        #Calendar
        self.calendar = QCalendarWidget()
        self.layout.addWidget(self.calendar)

        #SpinBox
        self.spin = QSpinBox()
        self.layout.addWidget(self.spin)

        #Tabs
        self.tabs = QTabWidget()
        self.tab1 = QWidget() # You can add any widget here
        self.tab2 = Window()
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.layout.addWidget(self.tabs)

        #ScrollArea and picture in it (you can add any widget)
        self.scroll = QScrollArea()
        pixmap = QPixmap('image.png')
        label = QLabel()
        label.setPixmap(pixmap)
        self.scroll.setWidget(label)
        self.layout.addWidget(self.scroll)

        #ProgressBar
        self.progress = QProgressBar()
        self.progress.setValue(24)
        self.layout.addWidget((self.progress))

        self.setLayout(self.layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example_window()
    sys.exit(app.exec())