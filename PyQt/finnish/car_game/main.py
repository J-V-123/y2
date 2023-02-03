from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from player import Player
from world import World
import sys

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(1200)            # asetetaan pääikkunan leveydeksi 1200
        self.setFixedHeight(980)            # asetetaan pääikkunan korkeudeksi 980
        self.init_game()

    def init_game(self):
        self.view = QGraphicsView()         # luodaan grafiikkanäkymä
        self.player = Player()              # luodaan itse pelihahmo (perii QGraphicsPolygonItemin)
        self.world = World(self.player, self.view)  # luodaan pelimaailma (perii QGraphicsScenen)

        self.setCentralWidget(self.view)    # asetetaan keskiwidgetiksi grafiikkanäkymä
        self.view.setScene(self.world)      # asetetaan grafiikkanäkymään pelimaailma
        self.view.setStyleSheet("background-image : url(background.png)")    # asetetaan taustakuva
        self.world.setSceneRect(0, 0, 1577, 980)    # asetetaan pelimaailmalle rajat (yhtäsuuri kuin taustan koko)

        self.world.addItem(self.player)     # lisätään pelaaja pelimaailmaan
        self.player.setPos(250, 485)        # asetetaan pelaaja koordinaatteihin 250, 485
        self.show()                         # näytetään pääikkuna

if __name__ == '__main__':
    app = QApplication(sys.argv)    # luodaan QApplication-olio
    game = Game()                   # luodaan Game-olio
    sys.exit(app.exec())            # jäädään odottamaan sovelluksen sulkeutumista