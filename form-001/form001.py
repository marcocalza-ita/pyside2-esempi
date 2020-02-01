from PySide2.QtWidgets import QApplication, QWidget
import sys

# versione di prova

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form1 di esempio")
        self.setGeometry(300,300, 500,400)
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)


myApp = QApplication(sys.argv)
window = Window()
window.show()

myApp.exec_()
sys.exit(0)
