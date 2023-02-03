import sys
from PyQt6.QtCore import QPointF, QRectF, Qt
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtWidgets import (QApplication, QGraphicsItem, QGraphicsScene,
                             QGraphicsView, QMainWindow)


class TicTacToe(QGraphicsItem):                                                   # inheriting QGraphicsItem class

    def __init__(self):
        super(TicTacToe, self).__init__()
        self.board = [[None, None, None], [None, None, None], [None, None, None]]  # creating a two-dimensional list for the board
        self.O = 0
        self.X = 1
        self.turn = self.O

    def boundingRect(self):                                                       # overwriting the method in base class which defines the borders of the graphics item
        return QRectF(0, 0, 300, 300)                                             # setting a square to be the borders

    def select(self, x, y):
        if x < 0 or y < 0 or x >= 3 or y >= 3:
            return
        if self.board[y][x] == None:                                              # if the square that was clicked is empty
            self.board[y][x] = self.turn                                         # adding 0 or X depending on whose turn was
            self.turn = 1 - self.turn                                            # changing the turn

    def paint(self, painter, option, widget):                                      # overwriting the paint() method of the base class
        painter.setPen(Qt.GlobalColor.black)                                       # setting a black pen for the painter
        painter.drawLine(0, 100, 300, 100)                                         # drawing the grid ( so redrawing everytime this method is called)
        painter.drawLine(0, 200, 300, 200)                                         # drawing a line from point (0, 200) to point (300, 200) and so on
        painter.drawLine(100, 0, 100, 300)
        painter.drawLine(200, 0, 200, 300)
        for y in range(3):                                                         # loop through the squares of the grid
            for x in range(3):
                if self.board[y][x] == self.O:                                      # if there is O in the square
                    painter.setPen(QPen(Qt.GlobalColor.red, 3))                    # setting a pen with the color red and width 3
                    painter.drawEllipse(QPointF(50+x*100, 50+y*100), 35, 35)       # and drawinf an ellipse
                elif self.board[y][x] == self.X:                                     #  if there is X in the square
                    painter.setPen(QPen(Qt.GlobalColor.blue, 3))                   # setting a pen with the color blue
                    painter.drawLine(20+x*100, 20+y*100, 80+x*100, 80+y*100)       # and drawing the first line of X
                    painter.drawLine(20+x*100, 80+y*100, 80+x*100, 20+y*100)       # and the second line

    def mousePressEvent(self, event):                                              # overwriting the method in base class, this is executed when the user clicks the screen
        self.select(int(event.pos().x()/100), int(event.pos().y()/100))            # the correct square is calcutaed from the location of the mouse click and the select() method above is called
        self.update()                                                              # updating the screen which results in paint() method to be called


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        scene = QGraphicsScene()                                                   # creating a scene
        view = QGraphicsView(scene)                                                # creating a view and giving the scene to it as a parameter
        self.setCentralWidget(view)                                                # setting the view to be the central widget
        self.setGeometry(0, 0, 320, 320)                                           # setting the size of the window
        self.tictactoe = TicTacToe()                                             # creating the game
        scene.addItem(self.tictactoe)                                             # adding the game to the scene
        self.show()                                                                # displaying the window


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec())

