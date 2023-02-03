from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QApplication, \
    QPushButton, QLabel, QVBoxLayout, QWidget, QSlider
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen, QCloseEvent, QGuiApplication
from spiral_calculator import calculate_coordinates
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()                 # luodaan windowille vertikaalinen asettelu
        self.setLayout(self.layout)                 # asetetaan luotu asettelu tämän windowin layoutiksi

        self.scene = QGraphicsScene()               # luodaan grafiikka-alue
        self.view = QGraphicsView(self.scene)       # luodaan näkymä, johon grafiikka-alue asetetaan
        self.layout.addWidget(self.view)            # lisätään näkymä asetteluun

        self.data = []                              # alustetaan self.data tyhjäksi listaksi
        self.view.scale(0.5, 0.5)                   # skaalataan näkymää hieman kauemmas, jotta varmistetaan, että
                                                    # näkymässä näkyy ikkunan avautuessa koko viivaspiraali

    def paintEvent(self, event):
        for i in self.data:
            line = QGraphicsLineItem(i[0], i[1], i[2], i[3])  # luodaan uusi viiva
            pen = QPen()  # luodaan uusi kynä
            pen.setWidthF(0.5)  # määritellään kynän leveys
            line.setPen(pen)  # määritetään viivan piirtyvän pen:iin asetetuilla määrityksillä
            self.scene.addItem(line)  # lisätään viiva grafiikka-alueseen

    def mousePressEvent(self, event):  # uudelleenmääritellään mousePressEvent()-metodi
        if event.button() == Qt.MouseButton.LeftButton:  # jos käyttäjä klikkaa hiiren vasemmalla näppäimellä
            self.view.scale(1.2, 1.2)  # skaalataan näkymä 1.2-kertaiseksi
        elif event.button() == Qt.MouseButton.RightButton:  # jos käyttäjä klikkaa hiiren oikealla näppäimellä
            self.view.scale(0.5, 0.5)  # skaalataan näkymä 0.5-kertaiseksi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Adjust the ratio")         # luodaan tekstikenttä
        self.button = QPushButton("Create a figure")    # luodaan nappula
        self.slider = QSlider()                         # luodaan liukusäädin
        self.slider.setMinimum(1)                       # asetetaan liukusäätimen vähimmäisarvo
        self.slider.setMaximum(600)                     # asetetaan liukusäätimen enimmäisarvo

        self.layout = QVBoxLayout()                     # luodaan pystysuuntainen asettelu
        self.layout.addWidget(self.label)               # lisätään tekstikenttä asetteluun
        self.layout.addWidget(self.slider)              # lisätään slideri asetteluun
        self.layout.addWidget(self.button)              # lisätään nappula asetteluun

        self.central_widget = QWidget()                 # luodaan uusi QWidget
        self.central_widget.setLayout(self.layout)      # asetetaan sen asetteluksi aiemmin luotu self.layout
        self.setCentralWidget(self.central_widget)      # asetaan se MainWindowin pääwidgetiksi

        self.button.clicked.connect(self.show_figure)   # yhdistetään signaali nappulan painamisesta metodiin show_figure
        self.showMaximized()                            # näytetään määrittelyt näytöllä

    def show_figure(self):
        self.window = Window()                                      # luodaan uusi ikkuna
        converted_value = 1 + float(self.slider.value() * 0.001)    # muunnettaan liukusäätimen arvo haluttuun muotoon
        self.window.data = calculate_coordinates(1000, 15, converted_value)     # lasketaan uudet koordinaatit

         # asetetaan avautuva ikkuna olevan 70% jäljellä olevasta tilasta
        self.window.resize(QGuiApplication.primaryScreen().availableGeometry().size() * 0.7)
        self.window.show()      # näytetään ikkuna

    def closeEvent(self, a0: QCloseEvent):
        if self.window:             # suljetaan avattu ikkuna, jos pääikkuna suljetaan
            self.window.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)    # luodaan QApplication-olio
    main_window = MainWindow()      # luodaan MainWindow-olio
    sys.exit(app.exec())            # jäädään odottamaan sovelluksen sulkeutumista