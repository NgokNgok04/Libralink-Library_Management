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
    QImage, QKeySequence, QLinearGradient, QPainter, QAction,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem, QFileDialog,
    QWidget)
import resources_rc
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 1080)
        MainWindow.setMinimumSize(QSize(1440, 1080))
        MainWindow.setMaximumSize(QSize(1440, 1080))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.headerWidget = QWidget(self.centralwidget)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setGeometry(QRect(0, 0, 1440, 178))
        self.headerWidget.setStyleSheet(u"background-color: rgb(109, 141, 223);")
        self.widget = QWidget(self.headerWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 338, 72))
        self.HLayoutLogo = QHBoxLayout(self.widget)
        self.HLayoutLogo.setObjectName(u"HLayoutLogo")
        self.HLayoutLogo.setContentsMargins(0, 0, 0, 0)
        self.logoLibraLink = QLabel(self.widget)
        self.logoLibraLink.setObjectName(u"logoLibraLink")
        self.logoLibraLink.setMinimumSize(QSize(70, 70))
        self.logoLibraLink.setMaximumSize(QSize(70, 70))
        self.logoLibraLink.setPixmap(QPixmap(u":/assets/libraLinkLogo.png"))

        self.HLayoutLogo.addWidget(self.logoLibraLink)

        self.logoTitle = QLabel(self.widget)
        self.logoTitle.setObjectName(u"logoTitle")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.logoTitle.setFont(font)
        self.logoTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.HLayoutLogo.addWidget(self.logoTitle)

        self.widget1 = QWidget(self.headerWidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(340, 125, 131, 36))
        self.horizontalLayout = QHBoxLayout(self.widget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.currentDirectory = QLabel(self.widget1)
        self.currentDirectory.setObjectName(u"currentDirectory")
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.currentDirectory.setFont(font1)
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
        self.profileName.setFont(font)
        self.profileName.setStyleSheet(u"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}")
        self.profileName.setAlignment(Qt.AlignCenter)
        self.admistrator = QPushButton(self.sidebarWidget)
        self.admistrator.setObjectName(u"admistrator")
        self.admistrator.setGeometry(QRect(90, 160, 141, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.admistrator.setFont(font2)
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
        icon1.addFile(u":/assets/homelogo2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HomeSidebar.setIcon(icon1)
        self.HomeSidebar.setIconSize(QSize(40, 40))
        self.HomeSidebar.setCheckable(True)
        self.HomeSidebar.setAutoExclusive(True)
        self.BukuSidebar = QPushButton(self.sidebarWidget)
        self.BukuSidebar.setObjectName(u"BukuSidebar")
        self.BukuSidebar.setGeometry(QRect(21, 311, 281, 50))
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
        icon2.addFile(u":/assets/daftarBukuLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.BukuSidebar.setIcon(icon2)
        self.BukuSidebar.setIconSize(QSize(40, 40))
        self.BukuSidebar.setCheckable(True)
        self.BukuSidebar.setAutoExclusive(True)
        self.AnggotaSidebar = QPushButton(self.sidebarWidget)
        self.AnggotaSidebar.setObjectName(u"AnggotaSidebar")
        self.AnggotaSidebar.setGeometry(QRect(21, 391, 281, 50))
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    
    def grab_all(self):
        # create a database or connect to one
        conn = sqlite3.connect('mylist.db')

        # create a cursor
        c = conn.cursor()
        # create a table
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        conn.commit()

        conn.close()
        for record in records:
            self.m

    
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
    # retranslateUi

