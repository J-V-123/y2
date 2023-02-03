import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QInputDialog  # tuodaan käytettävät luokat sovelluksen käytettäväksi


class Example_mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button1 = QPushButton('Show name input', self)     # creating a button
        self.button1.clicked.connect(self.show_dialog)          # connecting the click of the button to our show_dialog() method

        self.label = QLabel()                                   # creating an empty label

        self.main_widget = QWidget()                            # creating a central widget
        self.setCentralWidget(self.main_widget)                 # setting it to central widget

        self.layout = QVBoxLayout()                             # creating a layout
        self.layout.addWidget(self.label)                       # adding the label to the layout
        self.layout.addWidget(self.button1)                     # adding the button to the layout

        self.main_widget.setLayout(self.layout)

        self.show()

    def show_dialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name')   #open a text dialog that asks for the name

        if ok:                                                                     # if the second return value of the dialog was True
            self.label.setText("{} {}".format('Hello', text))                       # change the text of the label

        '''
        item, ok = QInputDialog.getItem(self, "Input dialog",
                                        "list of names", ["Roosa", "Daniel", "Olli"], 0, False)
        if ok and item:
              self.label.setText("{} {}".format('Hello', item))
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)  # creating the application object
    example = Example_mainwindow()
    sys.exit(app.exec())