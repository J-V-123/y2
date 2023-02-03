import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QRadioButton, \
    QLabel  # tuodaan käytettävät luokat sovelluksen käytettäväksi
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap


class Example_window(QWidget):
    def __init__(self):
        super().__init__()
        self.radiobutton1 = QRadioButton('Show picture', self)  # creating a radio button
        self.radiobutton2 = QRadioButton('Hide picture', self)
        self.button = QPushButton('Change to blue', self)  # creating a push button
        self.button.setStyleSheet("background-color : red;")
        self.checkbox = QCheckBox('Use custom title', self)  # creating a checkbox
        self.radiobutton2.move(0, 30)  # moving the buttons
        self.button.move(0, 80)
        self.checkbox.move(0, 140)
        self.setGeometry(20, 20, 700,
                         350)  # setting a size for the window by giving the coordinates of the left upper corner and width and the lenght of the window

        self.show()

        self.button.clicked.connect(
            self.button_clicked)  # connecting the act of clicking of the push button to our own method button_clicked()

        self.checkbox.stateChanged.connect(
            self.checkbox_clicked)  # connecting the changing of the state of the checkbox to our own method checkbox_clicked()

        self.radiobutton1.clicked.connect(
            self.radio_button_clicked)  # connecting the act of clicking of the radio button to our own method
        self.radiobutton2.clicked.connect(self.radio_button_clicked)

        # creating the picture. As this is after self.show() the picture is not displayed on the screen
        self.picture = QPixmap("image.png")  # creating a pixmap object for the picture
        self.picture = self.picture.scaledToHeight(300)  # changing the size. ScaledToHeight returns the scaled picture
        self.label_picture = QLabel(self)  # creating a label for the picture
        self.label_picture.move(300, 20)  # moving the label
        self.label_picture.setPixmap(self.picture)  # setting the picture to the label

    def button_clicked(self):
        if self.button.text() == "Change to blue":  # checking the text of the push button
            self.button.setStyleSheet("background-color : blue;")  # changing the color of the push button
            self.button.setText("Change to red")  # changing the text of the push button
        else:
            self.button.setStyleSheet("background-color : red;")
            self.button.setText("Change to blue")

    def checkbox_clicked(self, state):
        if self.checkbox.isChecked():  # checking if the checkbox is checked or not
            self.setWindowTitle('My own title')
        else:
            self.setWindowTitle('')

    def radio_button_clicked(self):
        if self.radiobutton1.isChecked():  # checking wether the radio button 1 or 2 is checked
            self.label_picture.show()  # diplaying the label, in which the picture is, on the screen
        else:
            self.label_picture.hide()  # hiding the label


if __name__ == '__main__':
    app = QApplication(sys.argv)  # creating the application object
    example = Example_window()  # creating the window
    sys.exit(app.exec())
