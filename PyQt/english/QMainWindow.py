import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextEdit, QDockWidget, QListWidget
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()                # creating a text edit area
        self.setCentralWidget(self.text_edit)       # setting it to be the central widget

        self.dock_widget = QDockWidget()             # creating a dock widget
        self.dock_widget.setWindowTitle('Dock')     # setting the title to 'Dock', otherwise it would be 'python' if the dock is taken out of the window

        self.listwidget = QListWidget()             # creating a list widget
        self.listwidget.addItem('Blueberry')        # adding items to list widget
        self.listwidget.addItem('Strawberry')
        self.listwidget.clicked.connect(self.clicked_dock_item)     # connecting the clicking of the list widget to our method

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock_widget)       # adding the dock widget to the main widget, the first parameter tells where in main widget it's placed
        self.dock_widget.setWidget(self.listwidget)                     # adding the list widget to the dock widget

        self.statusBar().setStatusTip('This is a statusbar')

        open_file = QAction(QIcon(None), 'Open new file', self)              # creating actions for the menubar
        open_file.setShortcut('Ctrl+F')
        open_file.setStatusTip('Open a new File')
        open_file.triggered.connect(self.show_dialog)

        edit_act = QAction(QIcon(None), '&Clear', self)
        edit_act.setShortcut('Ctrl+E')
        edit_act.setStatusTip('Clear the text field')
        edit_act.triggered.connect(self.clear_the_text_field)

        help_act = QAction(QIcon(None), '&Show help text', self)
        help_act.setShortcut('Ctrl+H')
        help_act.setStatusTip('Show the help guide')
        help_act.triggered.connect(self.show_help)

        menubar = self.menuBar()            # creating the menubar
        file_menu = menubar.addMenu('&File')        # adding the actions to the menubar
        file_menu.addAction(open_file)
        file_menu = menubar.addMenu('&Edit')
        file_menu.addAction(edit_act)
        file_menu = menubar.addMenu("&Help")
        file_menu.addAction(help_act)

        self.setGeometry(300, 300, 350, 250)            # setting size to the window
        self.setWindowTitle('A simple menu')            # and title
        self.show()                                     # dislaying mainwindow

    def show_dialog(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file')         # open a dialog where user can choose the name of the file
        if file_name[0]:
            file = open(file_name[0], 'r')                                  # opening the file
            with file:
                file_contents = file.read()
                self.text_edit.setText(file_contents)          # setting the content of the to the text edit area

    def show_help(self):
        self.text_edit.setText('This is an example how to use PyQt6 menu-bars and dialogs')

    def clear_the_text_field(self):
        self.text_edit.setText('')

    def clicked_dock_item(self):
        self.text_edit.setText(self.listwidget.currentItem().text())       # setting the text of the clicked item to the text edit area


def main():
    app = QApplication(sys.argv)
    example_window = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
