from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from components.Header import Header
from components.Sidebar import Sidebar
from components.AddButton import AddButton
from components.DaftarAnggotaPage import DaftarAnggotaPage
from components.DaftarPeminjaman import DaftarPeminjaman
from components.FormBuku import FormBuku
# from components.TemplateDaftarAnggota import TemplateDaftarAnggota

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("LibraLink Management")
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        print(screenSize)
        self.resize(screenSize.width(), screenSize.height())
        self.setMinimumSize(QSize(screenSize.width(), screenSize.height()))
        self.setMaximumSize(QSize(screenSize.width(), screenSize.height()))
        self.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.headerWidget = Header(self.centralwidget)
        self.sidebarWidget = Sidebar(self.centralwidget)

        self.sidebarWidget.showWidget.connect(self.headerWidget.changeStackedWidgetIndex)
        
        # page Daftar Anggota and Daftar Buku
        self.stackedWidgetPage = QStackedWidget(self.centralwidget)
        self.stackedWidgetPage.setGeometry(QRect(360, 178, screenSize.width() - 355, screenSize.height() - 240))
        # self.stackedWidgetPage.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.HomePage = QWidget()
        self.Daftar_BukuPage = QWidget()
        self.Daftar_AnggotaPage = DaftarAnggotaPage()

        self.stackedWidgetPage.addWidget(self.HomePage)
        self.stackedWidgetPage.addWidget(self.Daftar_BukuPage)
        self.stackedWidgetPage.addWidget(self.Daftar_AnggotaPage)
        self.stackedWidgetPage.setCurrentIndex(0)
        self.headerWidget.setContentsMargins(0, 0, 0, 0)
        self.addButton = AddButton(self.centralwidget)
        self.addButton.setGeometry(QRect(screenSize.width() - 80, screenSize.height() - 105, 70, 70))
        self.headerWidget.showAddButton.connect(self.addButton.isShowAddButton)
        self.headerWidget.showPageIndex.connect(self.whatPageToShow)

        self.DaftarPeminjaman = DaftarPeminjaman(self.centralwidget)
        self.DaftarPeminjaman.hide()
        self.DaftarPeminjaman.showDaftarPeminjaman.connect(self.IsShowDaftarPeminjaman)
        self.Daftar_AnggotaPage.showDaftarPeminjaman.connect(self.IsShowDaftarPeminjaman)

        self.formBuku = FormBuku(self.centralwidget)
        self.formBuku.show()

    @Slot(int)
    def whatPageToShow(self,index):
        self.stackedWidgetPage.setCurrentIndex(index)
        # self.addButton.raise_()
    
    @Slot(bool)
    def IsShowDaftarPeminjaman(self,isShow):
        if(isShow):
            self.DaftarPeminjaman.show()
        else:
            self.DaftarPeminjaman.hide()
