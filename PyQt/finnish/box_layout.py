import sys
# tuodaan käytettävät luokat sovelluksen käytettäväksi
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class Example_mainwindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('1')     # luodaan nappula tekstillä '1'
        self.button2 = QPushButton('2')
        self.button3 = QPushButton('3')
        self.button4 = QPushButton('4')

        self.main_widget = QWidget()        # luodaan pääwidget
        self.setCentralWidget(self.main_widget)     # asetetaan se pääwidgetiksi

        self.main_layout = QVBoxLayout()    # luodaan vertikaalinen asettelu, kuvassa sininen laatikko
        self.red_layout1 = QVBoxLayout()    # luodaan vertikaalinen asettelu, kuvassa ylempi punainen laatikko
        self.red_layout2 = QHBoxLayout()    # luodaan horisontaalinen asettelu, kuvassa alempi punainen laatikko

        self.main_layout.addLayout(self.red_layout1)    # lisätään "siniseen" laatikkoon "punaiset" laatikot
        self.main_layout.addLayout(self.red_layout2)

        self.red_layout1.addWidget(self.button1)        # lisätään "punaisiin" laatikoihin nappulat
        self.red_layout1.addWidget(self.button2)

        self.red_layout2.addWidget(self.button3)
        self.red_layout2.addWidget(self.button4)

        self.main_widget.setLayout(self.main_layout)     # aseteaan pääwidgetille "sininen" laatikko asetteluksi

        self.show()                                      # Päivittää ylläolevat määrittelyt näkymään ruudulle


if __name__ == '__main__':
    app = QApplication(sys.argv)                         # Luodaan QApplication-olio
    example = Example_mainwindow()
    sys.exit(app.exec())                                 # app.exec() aloittaa tapahtumankäsittelyn