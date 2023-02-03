import sys
from PyQt6.QtWidgets import QApplication, QWidget   # importing the classes we need from the library

def create_window():
    window = QWidget()                       # creating a QWidget-object to be our window
    window.setWindowTitle('Hello world!')    # setting the title for the window
    window.show()                           # show() method displays the widget on the screen
    sys.exit(app.exec())                    # app.exec() starts the application and it's event handling, which ends when the application gets closed
                                         # sys.exit()  method ensures a clean exit


if __name__ == '__main__':
    app = QApplication(sys.argv)    #  creating the application object
    create_window()                  # calling the function to create our window

