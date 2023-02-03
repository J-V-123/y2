from PyQt6.QtWidgets import QGraphicsScene
from PyQt6 import QtCore


class World(QGraphicsScene):                # peritään QGraphicsScene
    def __init__(self, player, view):
        super().__init__()
        self.player = player
        self.view = view
        self.timer = QtCore.QTimer()        # luodaan ajastin
        self.timer.start(int(1000 / 33))    # käynnistetään ajastin. se käynnistyy uudelleen joka 0.03. sekunti
        self.timer.timeout.connect(self.timerEvent)     # määritetään mitä tapahtuu, kun ajastin menee nollaan

    def keyPressEvent(self, event):                     # uudelleen määritellään keyPressEvent()-metodi
        if event.key() == QtCore.Qt.Key.Key_Right:
            self.player.moving_right = True             # asetetaan pelaaja liikkumaan oikealle
        if event.key() == QtCore.Qt.Key.Key_Left:
            self.player.moving_left = True              # asetetaan pelaaja liikkumaan vasemmalle

    def keyReleaseEvent(self, event):       # uudelleen määritellään keyReleaseEvent()-metodi
        if not event.isAutoRepeat():        # tarkistaan, että näppäin ei ole pidettynä pohjassa
            if event.key() == QtCore.Qt.Key.Key_Right:
                self.player.moving_right = False    # asetetaan pelaajan liikkuminen oikealle loppumaan
            if event.key() == QtCore.Qt.Key.Key_Left:
                self.player.moving_left = False     # asetetaan pelaajan liikkuminen vasemmalle loppumaan
            self.player.speed = 0                   # nollataan pelaajan nopeus

    # uudelleen määritellään timerEvent()-metodi, tätä kutsutaan automaattisesti, kun luomamme ajastin menee nollaan
    # tätä metodia kutsutaan siis joka 0.03. sekunti
    def timerEvent(self):
        self.player.update_velocities()             # kutsutaan pelaajan metodia, jossa päivitetään pelaajan nopeudet
        self.player.update_position()               # kutsutaan pelaajan metodia, jossa päivitetään pelaajan sijainti
        self.view.centerOn(self.player.scenePos())  # keskitetään näkymä pelaajaan
