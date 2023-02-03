

import sys
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QApplication

class Example_Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 300, 200) # setting the location and the size of the window

        self.qLabel = QLabel(self) # creating an empty label
        self.qLineEdit = QLineEdit(self) # creating a line edit widget
        self.qLineEdit.move(70, 50) # moving the line edit
        self.qLabel.move(70, 120) # moving the label

        self.qLineEdit.textChanged[str].connect(self.onChanged)   # connecting the change of text in the editor to execution of our onChanged() -method
        self.show()

    def onChanged(self, text):
        self.qLabel.setText(text) #setting the text for the label
        self.qLabel.adjustSize() # adjusting the size of the label so that the text will fit

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Example_Window()
    sys.exit(app.exec())
