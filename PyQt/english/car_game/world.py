from PyQt6.QtWidgets import QGraphicsScene
from PyQt6 import QtCore

class World(QGraphicsScene):            # inherits QGraphicsScene
    def __init__(self, player, view):
        super().__init__()
        self.player = player
        self.view = view
        self.timer = QtCore.QTimer()        # a timer is created
        self.timer.start(int(1000 / 33))    # the timer is started. it restarts every 0.03. second
        self.timer.timeout.connect(self.timerEvent)     # defines what happens when the timer goes to zero

    def keyPressEvent(self, event):                     # the keyPressEvent() method is redefined
        if event.key() == QtCore.Qt.Key.Key_Right:
            self.player.moving_right = True             # sets the player to move to the right
        if event.key() == QtCore.Qt.Key.Key_Left:
            self.player.moving_left = True              # sets the player to move left

    def keyReleaseEvent(self, event):       # the keyReleaseEvent() method is redefined
        if not event.isAutoRepeat():        # it is checked that the key is not held down
            if event.key() == QtCore.Qt.Key.Key_Right:
                self.player.moving_right = False    # sets the player's movement to the right to end
            if event.key() == QtCore.Qt.Key.Key_Left:
                self.player.moving_left = False     # sets the player's movement to the left to end
            self.player.speed = 0                   # set the player's speed to zero 

    # redefining the timerEvent() method, this will be called automatically when the timer we created goes to zero
    # this method is therefore called every 0.03. second
    def timerEvent(self):
        self.player.update_velocities()             # calls the player's method, that updates the player's speeds
        self.player.update_position()               # calls the player's method, that updates the player's position
        self.view.centerOn(self.player.scenePos())  # set the focus on the player