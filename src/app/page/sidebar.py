from home2 import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        self.icon_name_widget.setHidden(True)

        self.home_closed.clicked.connect(self.switch_to_homePage)
        self.home_open.clicked.connect(self.switch_to_homePage)
        
        self.buku_closed.clicked.connect(self.switch_to_daftarBukuPage)
        self.buku_open.clicked.connect(self.switch_to_daftarBukuPage)

        self.anggota_closed.clicked.connect(self.switch_to_daftarAnggotaPage)
        self.anggota_open.clicked.connect(self.switch_to_daftarAnggotaPage)
    
    def switch_to_homePage(self):
        print("test home")
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_daftarBukuPage(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_daftarAnggotaPage(self):
        self.stackedWidget.setCurrentIndex(2)