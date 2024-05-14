from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Sidebar(QWidget):

    showWidget = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        # define layout sidebar
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        self.layoutSidebar = QWidget(self)
        self.layoutSidebar.setGeometry(QRect(20, 120, 321, screenSize.height() - 180 ))
        # 1032 - 120 = 912
        self.layoutSidebar.setStyleSheet("border-radius: 10px; border: 2px solid rgb(100, 119, 219);")

        font = QFont()
        font.setPointSize(16)
        font.setBold(True)

        self.profileName = QLabel(self.layoutSidebar)
        self.profileName.setGeometry(QRect(71, 128, 178, 24))
        self.profileName.setFont(font)
        self.profileName.setStyleSheet(u"color: rgb(0, 0, 0); border: none;")
        self.profileName.setAlignment(Qt.AlignCenter)

        self.admistrator = QPushButton(self.layoutSidebar)
        self.admistrator.setGeometry(QRect(90, 160, 141, 31))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.admistrator.setFont(font2)
        self.admistrator.setStyleSheet(u"background-color: rgba(111, 207, 151, 51); color: rgb(111, 207, 151); border-radius: 15px; border: none; ")

        self.profileImage = QPushButton(self.layoutSidebar)
        self.profileImage.setGeometry(QRect(106, 22, 103, 99))
        self.profileImage.setStyleSheet(u"border:none;")

        icon = QIcon()
        icon.addFile(u"assets/profilePlaceHolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profileImage.setIcon(icon)
        self.profileImage.setIconSize(QSize(99, 99))

        self.HomeSidebar = QPushButton(self.layoutSidebar)
        self.HomeSidebar.setGeometry(QRect(21, 231, 281, 50))
        self.HomeSidebar.setFont(font)
        self.HomeSidebar.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	\n"
"	color: rgb(100, 119, 219);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"assets/homelogo2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeSidebar.setIcon(icon1)
        self.HomeSidebar.setIconSize(QSize(40, 40))
        self.HomeSidebar.setCheckable(True)
        self.HomeSidebar.setAutoExclusive(True)
        self.HomeSidebar.setChecked(True)
        self.HomeSidebar.clicked.connect(lambda: self.showWidget.emit(0))

        self.BukuSidebar = QPushButton(self.layoutSidebar)
        self.BukuSidebar.setGeometry(QRect(21, 291, 281, 50))
        self.BukuSidebar.setFont(font)
        self.BukuSidebar.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(100, 119, 219);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"assets/daftarBukuLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BukuSidebar.setIcon(icon2)
        self.BukuSidebar.setIconSize(QSize(40, 40))
        self.BukuSidebar.setCheckable(True)
        self.BukuSidebar.setAutoExclusive(True)
        self.BukuSidebar.clicked.connect(lambda: self.showWidget.emit(1))
        
        self.AnggotaSidebar = QPushButton(self.layoutSidebar)
        self.AnggotaSidebar.setGeometry(QRect(21, 351, 281, 50))
        self.AnggotaSidebar.setFont(font)
        self.AnggotaSidebar.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton:checked {\n"
"	\n"
"	color: rgb(100, 119, 219);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"assets/daftarAnggotaLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AnggotaSidebar.setIcon(icon3)
        self.AnggotaSidebar.setIconSize(QSize(40, 40))
        self.AnggotaSidebar.setCheckable(True)
        self.AnggotaSidebar.setAutoExclusive(True)
        self.AnggotaSidebar.clicked.connect(lambda: self.showWidget.emit(2))

        self.profileName.setText("Muhammad Zains")
        self.admistrator.setText("Administrator")
        self.profileImage.setText("")
        self.HomeSidebar.setText("Home")
        self.BukuSidebar.setText("Daftar Buku")
        self.AnggotaSidebar.setText("Daftar Anggota")

        