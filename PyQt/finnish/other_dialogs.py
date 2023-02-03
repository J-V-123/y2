import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QErrorMessage, QColorDialog, QFileDialog
from PyQt6.QtCore import Qt


class Example_window(QWidget):
    def __init__(self):
        super().__init__()

        # Huom! Tämä esimerkki ainoastaan aukaisee dialogit! Netistä löydät esimerkkejä, miten käsitellä dialogin antamaa tietoa
        # Attention! This example ONLY opens the dialogs! To actually do something with the information you can get from the dialogs,
        # check examples on the internet

        self.box = QMessageBox()
        self.box.setText("You chose to quit the game.")
        self.box.setInformativeText("Are you sure to quit the game?");
        self.box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Help | QMessageBox.StandardButton.Cancel)
        ret = self.box.exec()

        file_name = QFileDialog.getOpenFileName(self, 'Open file')

        self.erm = QErrorMessage()
        self.erm.showMessage("The file you tried to open was not the correct format!")
        self.erm.exec()

        color = QColorDialog.getColor()

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example_window()
    sys.exit(app.exec())
