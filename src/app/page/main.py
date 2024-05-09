from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from Home import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Window")


app = QApplication(sys.argv)

window = MySideBar()

window.show()

app.exec()