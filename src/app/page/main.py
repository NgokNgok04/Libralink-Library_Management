from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from DaftarAnggota import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Window")
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,100)
        self.tableWidget.setColumnWidth(3,200)


app = QApplication(sys.argv)

window = MySideBar()

window.show()

app.exec()