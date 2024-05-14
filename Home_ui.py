# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 1080)
        MainWindow.setMinimumSize(QSize(1440, 1080))
        MainWindow.setMaximumSize(QSize(1440, 1080))
        font = QFont()
        font.setBold(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.headerWidget = QWidget(self.centralwidget)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setGeometry(QRect(0, 0, 1440, 178))
        self.headerWidget.setStyleSheet(u"background-color: rgb(109, 141, 223);")
        self.layoutWidget = QWidget(self.headerWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 338, 72))
        self.HLayoutLogo = QHBoxLayout(self.layoutWidget)
        self.HLayoutLogo.setObjectName(u"HLayoutLogo")
        self.HLayoutLogo.setContentsMargins(0, 0, 0, 0)
        self.logoLibraLink = QLabel(self.layoutWidget)
        self.logoLibraLink.setObjectName(u"logoLibraLink")
        self.logoLibraLink.setMinimumSize(QSize(70, 70))
        self.logoLibraLink.setMaximumSize(QSize(70, 70))
        self.logoLibraLink.setPixmap(QPixmap(u":/assets/libraLinkLogo.png"))

        self.HLayoutLogo.addWidget(self.logoLibraLink)

        self.logoTitle = QLabel(self.layoutWidget)
        self.logoTitle.setObjectName(u"logoTitle")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.logoTitle.setFont(font1)
        self.logoTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.HLayoutLogo.addWidget(self.logoTitle)

        self.layoutWidget1 = QWidget(self.headerWidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(340, 125, 131, 36))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.currentDirectory = QLabel(self.layoutWidget1)
        self.currentDirectory.setObjectName(u"currentDirectory")
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        self.currentDirectory.setFont(font2)
        self.currentDirectory.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.currentDirectory)

        self.sidebarWidget = QWidget(self.centralwidget)
        self.sidebarWidget.setObjectName(u"sidebarWidget")
        self.sidebarWidget.setGeometry(QRect(30, 122, 321, 861))
        self.sidebarWidget.setStyleSheet(u"QWidget{\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(100, 119, 219);\n"
"}")
        self.profileName = QLabel(self.sidebarWidget)
        self.profileName.setObjectName(u"profileName")
        self.profileName.setGeometry(QRect(71, 128, 178, 24))
        self.profileName.setFont(font1)
        self.profileName.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}")
        self.profileName.setAlignment(Qt.AlignCenter)
        self.admistrator = QPushButton(self.sidebarWidget)
        self.admistrator.setObjectName(u"admistrator")
        self.admistrator.setGeometry(QRect(90, 160, 141, 31))
        font3 = QFont()
        font3.setPointSize(10)
        self.admistrator.setFont(font3)
        self.admistrator.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(111, 207, 151, 51);\n"
"	color: rgb(111, 207, 151);\n"
"	border-radius: 15px;\n"
"	border: none;\n"
"}")
        self.profileImage = QPushButton(self.sidebarWidget)
        self.profileImage.setObjectName(u"profileImage")
        self.profileImage.setGeometry(QRect(106, 22, 103, 99))
        self.profileImage.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/assets/profilePlaceHolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profileImage.setIcon(icon)
        self.profileImage.setIconSize(QSize(99, 99))
        self.HomeSidebar = QPushButton(self.sidebarWidget)
        self.HomeSidebar.setObjectName(u"HomeSidebar")
        self.HomeSidebar.setGeometry(QRect(21, 231, 281, 50))
        self.HomeSidebar.setFont(font1)
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
        icon1.addFile(u":/assets/homelogo2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeSidebar.setIcon(icon1)
        self.HomeSidebar.setIconSize(QSize(40, 40))
        self.HomeSidebar.setCheckable(True)
        self.HomeSidebar.setAutoExclusive(True)
        self.BukuSidebar = QPushButton(self.sidebarWidget)
        self.BukuSidebar.setObjectName(u"BukuSidebar")
        self.BukuSidebar.setGeometry(QRect(21, 311, 281, 50))
        self.BukuSidebar.setFont(font1)
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
        icon2.addFile(u":/assets/daftarBukuLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BukuSidebar.setIcon(icon2)
        self.BukuSidebar.setIconSize(QSize(40, 40))
        self.BukuSidebar.setCheckable(True)
        self.BukuSidebar.setAutoExclusive(True)
        self.AnggotaSidebar = QPushButton(self.sidebarWidget)
        self.AnggotaSidebar.setObjectName(u"AnggotaSidebar")
        self.AnggotaSidebar.setGeometry(QRect(21, 391, 281, 50))
        self.AnggotaSidebar.setFont(font1)
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
        icon3.addFile(u":/assets/daftarAnggotaLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AnggotaSidebar.setIcon(icon3)
        self.AnggotaSidebar.setIconSize(QSize(40, 40))
        self.AnggotaSidebar.setCheckable(True)
        self.AnggotaSidebar.setAutoExclusive(True)
        self.SearchBar = QWidget(self.centralwidget)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setGeometry(QRect(880, 190, 541, 41))
        self.inputSearch = QLineEdit(self.SearchBar)
        self.inputSearch.setObjectName(u"inputSearch")
        self.inputSearch.setGeometry(QRect(0, 0, 481, 41))
        self.inputSearch.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border: 1px solid rgb(100, 119, 219);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"	padding-left: 10px;\n"
"}")
        self.buttonSearch = QPushButton(self.SearchBar)
        self.buttonSearch.setObjectName(u"buttonSearch")
        self.buttonSearch.setGeometry(QRect(480, 0, 41, 41))
        self.buttonSearch.setStyleSheet(u"QPushButton{\n"
"	border-top: 1px solid rgb(100, 119, 219);\n"
"	border-right: 1px solid rgb(100, 119, 219);\n"
"	border-bottom: 1px solid rgb(100, 119, 219); \n"
"	border-top-right-radius: 17px;\n"
"	border-bottom-right-radius: 17px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets/searchFaceLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSearch.setIcon(icon4)
        self.buttonSearch.setIconSize(QSize(24, 24))
        self.FormBukuStackWidget = QStackedWidget(self.centralwidget)
        self.FormBukuStackWidget.setObjectName(u"FormBukuStackWidget")
        self.FormBukuStackWidget.setGeometry(QRect(360, 220, 381, 531))
        self.FormBukuStackWidget.setAutoFillBackground(False)
        self.FormBukuStackWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.FormDaftarBuku1 = QWidget()
        self.FormDaftarBuku1.setObjectName(u"FormDaftarBuku1")
        self.FormDaftarBuku1.setStyleSheet(u"Qwidget {\n"
" background-color: rgb(255, 255, 255);\n"
" border-top: 1px solid rgb(181, 181, 181);\n"
" border-right: 1px solid rgb(181, 181, 181);\n"
" border-bottom: 1px solid rgb(181, 181, 181);\n"
" border-top-right-radius: 10px;\n"
" border-bottom-right-radius: 10px;\n"
" border-top-left-radius: 10px;\n"
" border-bottom-left-radius: 10px;\n"
"}\n"
"")
        self.Simpan1 = QPushButton(self.FormDaftarBuku1)
        self.Simpan1.setObjectName(u"Simpan1")
        self.Simpan1.setGeometry(QRect(50, 430, 281, 50))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.Simpan1.setFont(font4)
        self.Simpan1.setLayoutDirection(Qt.LeftToRight)
        self.Simpan1.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(85, 85, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(85, 85, 255);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        self.Simpan1.setIconSize(QSize(40, 40))
        self.Simpan1.setCheckable(True)
        self.Simpan1.setAutoExclusive(True)
        self.Cover_buku1 = QPushButton(self.FormDaftarBuku1)
        self.Cover_buku1.setObjectName(u"Cover_buku1")
        self.Cover_buku1.setGeometry(QRect(50, 80, 281, 41))
        self.Cover_buku1.setFont(font4)
        self.Cover_buku1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0,0,0);\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 10px solid  rgb(214, 214, 214);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"   	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"   border: 1px solid rgb(214, 214, 214);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../../../../Vector.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Cover_buku1.setIcon(icon5)
        self.Cover_buku1.setIconSize(QSize(40, 40))
        self.Cover_buku1.setCheckable(True)
        self.Cover_buku1.setAutoExclusive(True)
        self.icon_judulbuku1 = QPushButton(self.FormDaftarBuku1)
        self.icon_judulbuku1.setObjectName(u"icon_judulbuku1")
        self.icon_judulbuku1.setGeometry(QRect(50, 140, 61, 41))
        self.icon_judulbuku1.setStyleSheet(u"QPushButton{\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-left: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214); \n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../../../../Vector (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_judulbuku1.setIcon(icon6)
        self.icon_judulbuku1.setIconSize(QSize(24, 24))
        self.JudulBuku1 = QLineEdit(self.FormDaftarBuku1)
        self.JudulBuku1.setObjectName(u"JudulBuku1")
        self.JudulBuku1.setGeometry(QRect(100, 140, 231, 41))
        font5 = QFont()
        font5.setPointSize(12)
        self.JudulBuku1.setFont(font5)
        self.JudulBuku1.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-right: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"	padding-left: 10px;\n"
"}")
        self.ISBN1 = QLineEdit(self.FormDaftarBuku1)
        self.ISBN1.setObjectName(u"ISBN1")
        self.ISBN1.setGeometry(QRect(100, 200, 231, 41))
        self.ISBN1.setFont(font5)
        self.ISBN1.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-right: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"	padding-left: 10px;\n"
"}")
        self.Icon_isbn1 = QPushButton(self.FormDaftarBuku1)
        self.Icon_isbn1.setObjectName(u"Icon_isbn1")
        self.Icon_isbn1.setGeometry(QRect(50, 200, 61, 41))
        self.Icon_isbn1.setStyleSheet(u"QPushButton{\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-left: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214); \n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../../../../tabler_number.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Icon_isbn1.setIcon(icon7)
        self.Icon_isbn1.setIconSize(QSize(24, 24))
        self.ID1 = QLineEdit(self.FormDaftarBuku1)
        self.ID1.setObjectName(u"ID1")
        self.ID1.setGeometry(QRect(100, 260, 231, 41))
        self.ID1.setFont(font5)
        self.ID1.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-right: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"	padding-left: 10px;\n"
"}")
        self.Icon_id1 = QPushButton(self.FormDaftarBuku1)
        self.Icon_id1.setObjectName(u"Icon_id1")
        self.Icon_id1.setGeometry(QRect(50, 260, 61, 41))
        self.Icon_id1.setStyleSheet(u"QPushButton{\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-left: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214); \n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../../../../Vector (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Icon_id1.setIcon(icon8)
        self.Icon_id1.setIconSize(QSize(24, 24))
        self.Upload = QPushButton(self.FormDaftarBuku1)
        self.Upload.setObjectName(u"Upload")
        self.Upload.setGeometry(QRect(240, 90, 81, 21))
        self.Upload.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: center;\n"
"    height: 30px;\n"
"    border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(134, 134, 134);\n"
"}\n"
"QPushButton:checked {\n"
"	\n"
"	color: rgb(100, 119, 219);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        self.Title1 = QLabel(self.FormDaftarBuku1)
        self.Title1.setObjectName(u"Title1")
        self.Title1.setGeometry(QRect(100, 10, 231, 41))
        font6 = QFont()
        font6.setFamilies([u"MS Shell Dlg 2"])
        font6.setPointSize(24)
        font6.setBold(False)
        font6.setItalic(False)
        self.Title1.setFont(font6)
        self.Title1.setStyleSheet(u"color: rgb(85, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"")
        self.FormBukuStackWidget.addWidget(self.FormDaftarBuku1)
        self.FormDaftarBuku2 = QWidget()
        self.FormDaftarBuku2.setObjectName(u"FormDaftarBuku2")
        self.Simpan2 = QPushButton(self.FormDaftarBuku2)
        self.Simpan2.setObjectName(u"Simpan2")
        self.Simpan2.setGeometry(QRect(50, 430, 281, 50))
        self.Simpan2.setFont(font4)
        self.Simpan2.setLayoutDirection(Qt.LeftToRight)
        self.Simpan2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(85, 85, 255);\n"
"}\n"
"QPushButton:checked {\n"
"	\n"
"	color: rgb(100, 119, 219);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        self.Simpan2.setIconSize(QSize(40, 40))
        self.Simpan2.setCheckable(True)
        self.Simpan2.setAutoExclusive(True)
        self.Title2 = QLabel(self.FormDaftarBuku2)
        self.Title2.setObjectName(u"Title2")
        self.Title2.setGeometry(QRect(100, 10, 231, 41))
        self.Title2.setFont(font6)
        self.Title2.setStyleSheet(u"color: rgb(85, 85, 255);\n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"")
        self.Judulbuku2 = QLineEdit(self.FormDaftarBuku2)
        self.Judulbuku2.setObjectName(u"Judulbuku2")
        self.Judulbuku2.setGeometry(QRect(100, 140, 231, 41))
        self.Judulbuku2.setFont(font5)
        self.Judulbuku2.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-right: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"	padding-left: 10px;\n"
"}")
        self.icon_judulbuku2 = QPushButton(self.FormDaftarBuku2)
        self.icon_judulbuku2.setObjectName(u"icon_judulbuku2")
        self.icon_judulbuku2.setGeometry(QRect(50, 140, 61, 41))
        self.icon_judulbuku2.setStyleSheet(u"QPushButton{\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-left: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214); \n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}")
        self.icon_judulbuku2.setIcon(icon6)
        self.icon_judulbuku2.setIconSize(QSize(24, 24))
        self.Icon_id2 = QPushButton(self.FormDaftarBuku2)
        self.Icon_id2.setObjectName(u"Icon_id2")
        self.Icon_id2.setGeometry(QRect(50, 260, 61, 41))
        self.Icon_id2.setStyleSheet(u"QPushButton{\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-left: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214); \n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}")
        self.Icon_id2.setIcon(icon8)
        self.Icon_id2.setIconSize(QSize(24, 24))
        self.ID2 = QLineEdit(self.FormDaftarBuku2)
        self.ID2.setObjectName(u"ID2")
        self.ID2.setGeometry(QRect(100, 260, 231, 41))
        self.ID2.setFont(font5)
        self.ID2.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-right: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"	padding-left: 10px;\n"
"}")
        self.HomeSidebar_3 = QPushButton(self.FormDaftarBuku2)
        self.HomeSidebar_3.setObjectName(u"HomeSidebar_3")
        self.HomeSidebar_3.setGeometry(QRect(50, 80, 281, 41))
        self.HomeSidebar_3.setFont(font4)
        self.HomeSidebar_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0,0,0);\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 10px solid  rgb(214, 214, 214);\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"   	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"   border: 1px solid rgb(214, 214, 214);\n"
"}")
        self.HomeSidebar_3.setIcon(icon5)
        self.HomeSidebar_3.setIconSize(QSize(40, 40))
        self.HomeSidebar_3.setCheckable(True)
        self.HomeSidebar_3.setAutoExclusive(True)
        self.Isbn2 = QLineEdit(self.FormDaftarBuku2)
        self.Isbn2.setObjectName(u"Isbn2")
        self.Isbn2.setGeometry(QRect(100, 200, 231, 41))
        self.Isbn2.setFont(font5)
        self.Isbn2.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-right: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214);\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"	padding-left: 10px;\n"
"}")
        self.Icon_isbn2 = QPushButton(self.FormDaftarBuku2)
        self.Icon_isbn2.setObjectName(u"Icon_isbn2")
        self.Icon_isbn2.setGeometry(QRect(50, 200, 61, 41))
        self.Icon_isbn2.setStyleSheet(u"QPushButton{\n"
"	border-top: 1px solid rgb(214, 214, 214);\n"
"	border-left: 1px solid rgb(214, 214, 214);\n"
"	border-bottom: 1px solid rgb(214, 214, 214); \n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}")
        self.Icon_isbn2.setIcon(icon7)
        self.Icon_isbn2.setIconSize(QSize(24, 24))
        self.Uploaded = QPushButton(self.FormDaftarBuku2)
        self.Uploaded.setObjectName(u"Uploaded")
        self.Uploaded.setGeometry(QRect(220, 90, 101, 21))
        self.Uploaded.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: center;\n"
"    height: 30px;\n"
"    border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(134, 134, 134);\n"
"	background-color: rgb(0, 190, 0);\n"
"}\n"
"QPushButton:checked {\n"
"	\n"
"	color: rgb(100, 119, 219);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        self.FormBukuStackWidget.addWidget(self.FormDaftarBuku2)
        self.DeleteWidget = QStackedWidget(self.centralwidget)
        self.DeleteWidget.setObjectName(u"DeleteWidget")
        self.DeleteWidget.setGeometry(QRect(800, 410, 491, 221))
        self.DeleteWidget.setStyleSheet(u"background-color: rgb(90, 90, 90);\n"
"")
        self.DeleteAnggota = QWidget()
        self.DeleteAnggota.setObjectName(u"DeleteAnggota")
        self.DeleteAnggota.setStyleSheet(u"Qwidget {\n"
" border-top: 1px solid rgb(214, 214, 214);\n"
" border-right: 1px solid rgb(214, 214, 214);\n"
" border-bottom: 1px solid rgb(214, 214, 214);\n"
" border-top-right-radius: 10px;\n"
" border-bottom-right-radius: 10px;\n"
" border-top-left-radius: 10px;\n"
" border-bottom-left-radius: 10px;\n"
"}")
        self.label = QLabel(self.DeleteAnggota)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 0, 261, 61))
        self.label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.DeleteAnggota)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 50, 261, 61))
        self.label_2.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Batal1 = QPushButton(self.DeleteAnggota)
        self.Batal1.setObjectName(u"Batal1")
        self.Batal1.setGeometry(QRect(40, 140, 161, 51))
        self.Batal1.setFont(font4)
        self.Batal1.setLayoutDirection(Qt.LeftToRight)
        self.Batal1.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(255, 60, 12);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        self.Batal1.setIconSize(QSize(40, 40))
        self.Batal1.setCheckable(True)
        self.Batal1.setAutoExclusive(True)
        self.Ya1 = QPushButton(self.DeleteAnggota)
        self.Ya1.setObjectName(u"Ya1")
        self.Ya1.setGeometry(QRect(270, 140, 161, 51))
        self.Ya1.setFont(font4)
        self.Ya1.setLayoutDirection(Qt.LeftToRight)
        self.Ya1.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(0, 170, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(0, 170, 0);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        self.Ya1.setIconSize(QSize(40, 40))
        self.Ya1.setCheckable(True)
        self.Ya1.setAutoExclusive(True)
        self.DeleteWidget.addWidget(self.DeleteAnggota)
        self.DeleteBukudanPeminjaman = QWidget()
        self.DeleteBukudanPeminjaman.setObjectName(u"DeleteBukudanPeminjaman")
        self.Ya1_2 = QPushButton(self.DeleteBukudanPeminjaman)
        self.Ya1_2.setObjectName(u"Ya1_2")
        self.Ya1_2.setGeometry(QRect(270, 140, 161, 51))
        self.Ya1_2.setFont(font4)
        self.Ya1_2.setLayoutDirection(Qt.LeftToRight)
        self.Ya1_2.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(0, 170, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(0, 170, 0);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        self.Ya1_2.setIconSize(QSize(40, 40))
        self.Ya1_2.setCheckable(True)
        self.Ya1_2.setAutoExclusive(True)
        self.label_4 = QLabel(self.DeleteBukudanPeminjaman)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 50, 261, 61))
        self.label_4.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.Batal1_2 = QPushButton(self.DeleteBukudanPeminjaman)
        self.Batal1_2.setObjectName(u"Batal1_2")
        self.Batal1_2.setGeometry(QRect(40, 140, 161, 51))
        self.Batal1_2.setFont(font4)
        self.Batal1_2.setLayoutDirection(Qt.LeftToRight)
        self.Batal1_2.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(255, 60, 12);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:checked {\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        self.Batal1_2.setIconSize(QSize(40, 40))
        self.Batal1_2.setCheckable(True)
        self.Batal1_2.setAutoExclusive(True)
        self.label_3 = QLabel(self.DeleteBukudanPeminjaman)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 0, 261, 61))
        self.label_3.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.DeleteWidget.addWidget(self.DeleteBukudanPeminjaman)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.FormBukuStackWidget.setCurrentIndex(0)
        self.DeleteWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLibraLink.setText("")
        self.logoTitle.setText(QCoreApplication.translate("MainWindow", u"Libralink Management", None))
        self.currentDirectory.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profileName.setText(QCoreApplication.translate("MainWindow", u"Muhammad Zains", None))
        self.admistrator.setText(QCoreApplication.translate("MainWindow", u"Administrator", None))
        self.profileImage.setText("")
        self.HomeSidebar.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.BukuSidebar.setText(QCoreApplication.translate("MainWindow", u"Daftar Buku", None))
        self.AnggotaSidebar.setText(QCoreApplication.translate("MainWindow", u"Daftar Anggota", None))
        self.inputSearch.setText("")
        self.inputSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cari Judul Buku, Penulis, Anggota", None))
        self.buttonSearch.setText("")
        self.Simpan1.setText(QCoreApplication.translate("MainWindow", u"                   Simpan", None))
        self.Cover_buku1.setText(QCoreApplication.translate("MainWindow", u"   Cover Buku", None))
        self.icon_judulbuku1.setText("")
        self.JudulBuku1.setText(QCoreApplication.translate("MainWindow", u"Judul Buku", None))
        self.JudulBuku1.setPlaceholderText("")
        self.ISBN1.setText(QCoreApplication.translate("MainWindow", u"Kode ISBN", None))
        self.ISBN1.setPlaceholderText("")
        self.Icon_isbn1.setText("")
        self.ID1.setText(QCoreApplication.translate("MainWindow", u"ID Buku", None))
        self.ID1.setPlaceholderText("")
        self.Icon_id1.setText("")
        self.Upload.setText(QCoreApplication.translate("MainWindow", u"Upload File JPG", None))
        self.Title1.setText(QCoreApplication.translate("MainWindow", u"FORM BUKU", None))
        self.Simpan2.setText(QCoreApplication.translate("MainWindow", u"		                SIMPAN", None))
        self.Title2.setText(QCoreApplication.translate("MainWindow", u"FORM BUKU", None))
        self.Judulbuku2.setText(QCoreApplication.translate("MainWindow", u"Cosmos", None))
        self.Judulbuku2.setPlaceholderText("")
        self.icon_judulbuku2.setText("")
        self.Icon_id2.setText("")
        self.ID2.setText(QCoreApplication.translate("MainWindow", u"03", None))
        self.ID2.setPlaceholderText("")
        self.HomeSidebar_3.setText(QCoreApplication.translate("MainWindow", u"   Cover Buku", None))
        self.Isbn2.setText(QCoreApplication.translate("MainWindow", u"842-0903-01-94", None))
        self.Isbn2.setPlaceholderText("")
        self.Icon_isbn2.setText("")
        self.Uploaded.setText(QCoreApplication.translate("MainWindow", u"File Uploaded", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Apakah Anda yakin ingin", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"menghapus anggota ini?", None))
        self.Batal1.setText(QCoreApplication.translate("MainWindow", u"       Batal", None))
        self.Ya1.setText(QCoreApplication.translate("MainWindow", u"           Ya", None))
        self.Ya1_2.setText(QCoreApplication.translate("MainWindow", u"           Ya", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"menghapus buku ini?", None))
        self.Batal1_2.setText(QCoreApplication.translate("MainWindow", u"       Batal", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Apakah Anda yakin ingin", None))
    # retranslateUi

