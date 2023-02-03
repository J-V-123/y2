from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsLineItem, QApplication, \
    QLabel, QVBoxLayout, QWidget, QSlider, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QColor
from spiral_calculator import calculate_coordinates
import sys

class Figure(QGraphicsScene):
    def __init__(self, view, ratio, lines, width):
        super().__init__()
        self.data = []                                                      # alustetaan self.data tyhjäksi listaksi
        self.pen_width = width                                              # asetetaan self.pen_width olevan width
        self.view = view                                                    # asetetaan self.view olevan view
        self.ratio = ratio                                                  # asetetaan self.view olevan ratio
        self.data = calculate_coordinates(1000, lines, ratio)               # lasketaan koordinaatit
        self.paint_lines()                                                  # kutsutaan metodia paint_lines, jossa piirrettään viivat

    def paint_lines(self):                                      # HUOM, tämä ei ole QGraphicsScenen valmis metodi
        for i in self.data:
            line = QGraphicsLineItem(i[0], i[1], i[2], i[3])    # luodaan uusi viiva
            pen = QPen()                                        # luodaan uusi kynä
            if 1.6 <= self.ratio <= 1.63:                       # jos ollaan likimain kultaisen leikkauksen alueella
                pen.setColor(QColor(255, 215, 0))               # väritetään viiva kultaiseksi
            pen.setWidthF(self.pen_width)                       # määritellään kynän leveys
            line.setPen(pen)                                    # määritetään viivan piirtyvän 'pen':iin asetetuilla määrityksillä
            self.addItem(line)                                  # lisätään viiva grafiikka-alueseen

    def mousePressEvent(self, event):                           # uudelleenmääritellään mousePressEvent()-metodi
        if event.button() == Qt.MouseButton.LeftButton:         # jos käyttäjä klikkaa hiiren vasemmalla näppäimellä
            self.view.scale(1.2, 1.2)                           # skaalataan näkymä 1.2-kertaiseksi
        elif event.button() == Qt.MouseButton.RightButton:      # jos käyttäjä klikkaa hiiren oikealla näppäimellä
            self.view.scale(0.5, 0.5)                           # skaalataan näkymä 0.5-kertaiseksi

class MainWindow(QWidget):      # MainWindow ei peri nyt luokkaa QMainWindow vaan luokan QWidget
    def __init__(self):
        super().__init__()

        self.ratio_slider = QSlider(Qt.Orientation.Horizontal)      # luodaan liukusäädin vaakasuunnassa
        self.ratio_slider.setMinimum(1)                             # asetetaan vähimmäisarvo
        self.ratio_slider.setMaximum(2000)                          # asetetaan enimmäisarvo
        self.ratio_slider.setValue(300)                             # asetetaan nykyiseksi arvoksi 300

        self.line_slider = QSlider(Qt.Orientation.Horizontal)       # toistetaan sama kuin yllä, mutta nyt viivoille
        self.line_slider.setMinimum(5)
        self.line_slider.setMaximum(500)

        self.pen_slider = QSlider(Qt.Orientation.Horizontal)
        self.pen_slider.setMinimum(1)
        self.pen_slider.setMaximum(20)
        self.pen_slider.setValue(10)

        self.container = QVBoxLayout()                              # luodaan pystysuuntainen asettelu

        self.ratio_label = QLabel()                                 # luodaan QLabel()-oliot liukusäätimien arvoille
        self.line_label = QLabel()
        self.pen_label = QLabel()

        self.calculate_and_set_values()                             # käytetään metodia self.calculate_and_set_values()

        self.ratio_container = QHBoxLayout()                        # luodaan suhteelle oma vaakasuuntainen asettelu
        self.ratio_container.addWidget(QLabel("Adjust the ratio"))  # lisätään asetteluun QLabel()
        self.ratio_container.addWidget(self.ratio_slider)           # lisätään liukusäädin asetteluun
        self.ratio_container.addWidget(self.ratio_label)            # lisätään self.ratio_label, joka näyttää nykyisen suhteen arvon

        self.line_container = QHBoxLayout()                         # toistetaan sama kuin yllä, mutta nyt viivoille
        self.line_container.addWidget(QLabel("Adjust the amount of lines"))
        self.line_container.addWidget(self.line_slider)
        self.line_container.addWidget(self.line_label)

        self.pen_container = QHBoxLayout()
        self.pen_container.addWidget(QLabel("Adjust the width of line"))
        self.pen_container.addWidget(self.pen_slider)
        self.pen_container.addWidget(self.pen_label)

        self.view = QGraphicsView()                                                             # luodaan uusi näkymä
        self.view.scale(0.7, 0.7)                                                               # skaalataan näkymää 0.7-kertaiseksi
        self.figure = Figure(self.view, self.ratio_value, self.line_value, self.pen_value)      # luodaan uusi Figure()
        self.view.setScene(self.figure)                                                         # asetetaan Figure näkymään

        self.container.addLayout(self.ratio_container)              # lisätään suhteen asettelu asetteluun self.container
        self.container.addLayout(self.line_container)               # lisätään viivojen asettelu asetteluun self.container
        self.container.addLayout(self.pen_container)                # lisätään kynän asettelu asetteluun self.container
        self.container.addWidget(self.view)                         # lisätään itse näkymä asetteluun self.container

        self.setLayout(self.container)                              # asetetaan self.container tämän ikkunan asetteluksi

        self.ratio_slider.valueChanged.connect(self.update_figure)  # yhdistetään signaalit, jos liukusäätimien arvot muuttuvat
        self.line_slider.valueChanged.connect(self.update_figure)
        self.pen_slider.valueChanged.connect(self.update_figure)
        self.showMaximized()                                        # näytetään määrittelyt näytöllä

    def update_figure(self):
        self.calculate_and_set_values()                                                     # lasketaan ja asetetaan uudet arvot
        self.figure = Figure(self.view, self.ratio_value, self.line_value, self.pen_value)  # luodaan uusi Figure
        self.view.setScene(self.figure)                                                     # lisätään se näkymään

    def calculate_and_set_values(self):     # tässä metodissa lasketaan uudet arvot ja asetetaan ne kukin omaan QLabeliin
        self.ratio_value = 1 + float(self.ratio_slider.value() * 0.001)
        self.line_value = self.line_slider.value()
        self.pen_value = self.pen_slider.value() / 10

        self.ratio_label.setNum(self.ratio_value)
        self.line_label.setNum(self.line_value)
        self.pen_label.setNum(self.pen_value)

if __name__ == '__main__':
    app = QApplication(sys.argv)    # luodaan QApplication-olio
    main_window = MainWindow()      # luodaan MainWindow()-olio
    sys.exit(app.exec())            # jäädään odottamaan sovelluksen sulkeutumista