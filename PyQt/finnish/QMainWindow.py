import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextEdit, QDockWidget, QListWidget
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()  # luodaan text edit olio
        self.setCentralWidget(self.text_edit)  # asetetaan se central widgetiksi

        self.dock_widget = QDockWidget()  # luodaan dock widget olio

        # astetetaan dockin titleksi 'Dock', muuten title olisi python jos dock irroitettaan ikkunasta
        self.dock_widget.setWindowTitle('Dock')

        self.listwidget = QListWidget()  # luodaan list widget olio
        self.listwidget.addItem('Blueberry')  # lisätään list widgettiin itemejä
        self.listwidget.addItem('Strawberry')

        # kun list widgettiä klikataan, tapahtuu jotain ->
        self.listwidget.clicked.connect(self.clicked_dock_item)

        # lisätään qmainwindowiin dockwidgetti. ensimmäinen parametri kertoo, minne dock asettuu
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dock_widget)

        # asetetaan dock widgettiin list widgetti
        self.dock_widget.setWidget(self.listwidget)

        self.statusBar().setStatusTip('This is a statusbar')

        open_file = QAction(QIcon(None), 'Open new file', self)  # luodaan qmenubariin nappulat
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

        menubar = self.menuBar()  # luodaan itse menu bar olio
        file_menu = menubar.addMenu('&File')  # lisätään menubariin äsken luodut nappulat
        file_menu.addAction(open_file)
        file_menu = menubar.addMenu('&Edit')
        file_menu.addAction(edit_act)
        file_menu = menubar.addMenu("&Help")
        file_menu.addAction(help_act)

        self.setGeometry(300, 300, 350, 250)  # asetetaan qmainwindowin geometria
        self.setWindowTitle('A simple menu')  # ja otsikko
        self.show()  # näytetään qmainwindow

    def show_dialog(self):
        # avataan dialogi, jossa käyttäjä voi valita tiedoston nimen
        file_name = QFileDialog.getOpenFileName(self, 'Open file')
        if file_name[0]:
            file = open(file_name[0], 'r')
            with file:
                file_contents = file.read()
                # asetetaan text editin paikalle avatun tiedoston sisältö
                self.text_edit.setText(file_contents)

    def show_help(self):
        self.text_edit.setText('This is an example how to use PyQt6 menu-bars and dialogs')

    def clear_the_text_field(self):
        self.text_edit.setText('')

    def clicked_dock_item(self):
        # asetetaan text editin paikalle klikatun itemin teksti
        self.text_edit.setText(self.listwidget.currentItem().text())


def main():
    app = QApplication(sys.argv)
    example_window = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
