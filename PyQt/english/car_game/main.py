from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from player import Player
from world import World
import sys

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(1200)            # sets the width of the main window to 1200
        self.setFixedHeight(980)            # sets the height of the main window to 980
        self.init_game()

    def init_game(self):
        self.view = QGraphicsView()         # a graphics view is created
        self.player = Player()              # create the game character itself (inherits QGraphicsPolygonItem)
        self.world = World(self.player, self.view)  # creating a Game World (inherits from QGraphicsScene)

        self.setCentralWidget(self.view)    # the graphics view is set as the middle widget
        self.view.setScene(self.world)      # sets the game world in graphics view
        self.view.setStyleSheet("background-image : url(background.png)")    # sets the background image

        # limits are set for the game world (the same size as the background size)
        self.world.setSceneRect(0, 0, 1577, 980)    

        self.world.addItem(self.player)     # a player is added to the game world
        self.player.setPos(250, 485)        # sets the player at coordinates 250, 485
        self.show()                         # the main window is displayed

if __name__ == '__main__':
    app = QApplication(sys.argv)    
    game = Game()                   
    sys.exit(app.exec()) 