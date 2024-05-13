
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import page.resources

class Header(QWidget):

    showAddButton = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        print(screenSize)

        # Widget Header ampe mentok
        self.layoutHeader = QWidget(self)
        self.layoutHeader.setStyleSheet(u"background-color: rgb(109, 141, 223);")
        self.layoutHeader.setGeometry(QRect(0, 0, screenSize.width(), 178))
        
        # Widget Layout Logo 338x72
        self.layoutLogo = QWidget(self.layoutHeader)
        self.layoutLogo.setGeometry(QRect(30, 20, 338, 72))

        # Widget didalam LayoutLogo
        self.HLayoutLogo = QHBoxLayout(self.layoutLogo)
        self.HLayoutLogo.setContentsMargins(0, 0, 0, 0)

        # insert gambar logo ke label didalam HLayoutLogo
        self.logoLibraLink = QLabel(self.layoutLogo)
        self.logoLibraLink.setText("")
        self.logoLibraLink.setMinimumSize(QSize(70, 70))
        self.logoLibraLink.setMaximumSize(QSize(70, 70))
        self.logoLibraLink.setPixmap(QPixmap(u":/assets/libraLinkLogo.png"))
        self.HLayoutLogo.addWidget(self.logoLibraLink)

        # insert tulisan title ke label didalam HLayoutLogo
        self.logoTitle = QLabel(self.layoutLogo)
        self.logoTitle.setText("LibraLink Management")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.logoTitle.setFont(font)
        self.logoTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.HLayoutLogo.addWidget(self.logoTitle)

        self.stackedWidgetDirectory = QStackedWidget(self.layoutHeader)
        self.stackedWidgetDirectory.setGeometry(QRect(360, 120, 481, 61))

        self.HomeDirectory = QWidget()

        self.HomeLabel = QLabel(self.HomeDirectory)
        self.HomeLabel.setText("Home")
        self.HomeLabel.setGeometry(QRect(10, 10, 101, 41))

        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.HomeLabel.setFont(font1)
        self.HomeLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.HomeDirectory)

        self.DaftarBukuDirectory = QWidget()

        self.DaftarBukuLabel = QLabel(self.DaftarBukuDirectory)
        self.DaftarBukuLabel.setText("Daftar Buku Perpustakaan")
        self.DaftarBukuLabel.setGeometry(QRect(10, 10, 381, 41))
        self.DaftarBukuLabel.setFont(font1)
        self.DaftarBukuLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.DaftarBukuDirectory)

        self.DaftarAnggotaDirectory = QWidget()

        self.DaftarAnggotaLabel = QLabel(self.DaftarAnggotaDirectory)
        self.DaftarAnggotaLabel.setText("Daftar Anggota Perpustakaaan")
        self.DaftarAnggotaLabel.setGeometry(QRect(10, 10, 431, 41))
        self.DaftarAnggotaLabel.setFont(font1)
        self.DaftarAnggotaLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.DaftarAnggotaDirectory)
        self.stackedWidgetDirectory.setCurrentIndex(0)
    
    @Slot(int)
    def changeStackedWidgetIndex(self,index):
        self.stackedWidgetDirectory.setCurrentIndex(index)
        if index == 1 or index == 2:
            self.showAddButton.emit(True)
        else:
            self.showAddButton.emit(False)