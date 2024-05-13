# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DaftarAnggota.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 780)
        MainWindow.setMinimumSize(QSize(1440, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.headerWidget = QWidget(self.centralwidget)
        self.headerWidget.setObjectName(u"headerWidget")
        self.headerWidget.setGeometry(QRect(0, 0, 1451, 171))
        self.headerWidget.setStyleSheet(u"background-color: rgb(109, 141, 223);")
        self.stackedWidgetDirectory = QStackedWidget(self.headerWidget)
        self.stackedWidgetDirectory.setObjectName(u"stackedWidgetDirectory")
        self.stackedWidgetDirectory.setGeometry(QRect(340, 110, 431, 61))
        self.HomeDirectory = QWidget()
        self.HomeDirectory.setObjectName(u"HomeDirectory")
        self.HomeLabel = QLabel(self.HomeDirectory)
        self.HomeLabel.setObjectName(u"HomeLabel")
        self.HomeLabel.setGeometry(QRect(10, 10, 101, 41))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.HomeLabel.setFont(font)
        self.HomeLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.HomeDirectory)
        self.DaftarBukuDirectory = QWidget()
        self.DaftarBukuDirectory.setObjectName(u"DaftarBukuDirectory")
        self.DaftarBukuLabel = QLabel(self.DaftarBukuDirectory)
        self.DaftarBukuLabel.setObjectName(u"DaftarBukuLabel")
        self.DaftarBukuLabel.setGeometry(QRect(10, 10, 381, 41))
        self.DaftarBukuLabel.setFont(font)
        self.DaftarBukuLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.DaftarBukuDirectory)
        self.DaftarAnggotaDirectory = QWidget()
        self.DaftarAnggotaDirectory.setObjectName(u"DaftarAnggotaDirectory")
        self.DaftarAnggotaLabel = QLabel(self.DaftarAnggotaDirectory)
        self.DaftarAnggotaLabel.setObjectName(u"DaftarAnggotaLabel")
        self.DaftarAnggotaLabel.setGeometry(QRect(10, 10, 431, 41))
        self.DaftarAnggotaLabel.setFont(font)
        self.DaftarAnggotaLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.DaftarAnggotaDirectory)
        self.widget = QWidget(self.headerWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 304, 72))
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
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.logoTitle.setFont(font1)
        self.logoTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.HLayoutLogo.addWidget(self.logoTitle)

        self.sidebarWidget = QWidget(self.centralwidget)
        self.sidebarWidget.setObjectName(u"sidebarWidget")
        self.sidebarWidget.setGeometry(QRect(20, 120, 321, 651))
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
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(340, 180, 1181, 591))
        self.stackedWidget.setStyleSheet(u"")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.stackedWidget.addWidget(self.Home)
        self.Daftar_Buku = QWidget()
        self.Daftar_Buku.setObjectName(u"Daftar_Buku")
        self.stackedWidget.addWidget(self.Daftar_Buku)
        self.Daftar_Anggota = QWidget()
        self.Daftar_Anggota.setObjectName(u"Daftar_Anggota")
        self.SearchBar = QWidget(self.Daftar_Anggota)
        self.SearchBar.setObjectName(u"SearchBar")
        self.SearchBar.setGeometry(QRect(610, 0, 541, 41))
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
"	background-color: rgb(255, 255, 255);\n"
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
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets/searchFaceLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSearch.setIcon(icon4)
        self.buttonSearch.setIconSize(QSize(24, 24))
        self.tableWidget = QTableWidget(self.Daftar_Anggota)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 50, 1121, 501))
        self.tableWidget.setMinimumSize(QSize(1021, 192))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(False)
        self.tableWidget.setFont(font3)
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	color: rgb(130, 130, 130);\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget{\n"
"	text-align: center;\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(153)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.AddButton = QPushButton(self.Daftar_Anggota)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(1110, 520, 70, 70))
        self.AddButton.setStyleSheet(u"QPushButton{\n"
"	border: none;	\n"
"	border-radius: 35px;\n"
"	\n"
"	background-color: rgb(109, 141, 223);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/assets/addButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddButton.setIcon(icon5)
        self.AddButton.setIconSize(QSize(34, 34))
        self.AddButton.setCheckable(True)
        self.AddButton.setAutoExclusive(False)
        self.widget1 = QWidget(self.Daftar_Anggota)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(210, 0, 71, 41))
        self.stackedWidget.addWidget(self.Daftar_Anggota)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidgetDirectory.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(2)
        self.AddButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HomeLabel.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.DaftarBukuLabel.setText(QCoreApplication.translate("MainWindow", u"Daftar Buku Perpustakaan", None))
        self.DaftarAnggotaLabel.setText(QCoreApplication.translate("MainWindow", u"Daftar Anggota Perpustakaan", None))
        self.logoLibraLink.setText("")
        self.logoTitle.setText(QCoreApplication.translate("MainWindow", u"Libralink Management", None))
        self.profileName.setText(QCoreApplication.translate("MainWindow", u"Muhammad Zains", None))
        self.admistrator.setText(QCoreApplication.translate("MainWindow", u"Administrator", None))
        self.profileImage.setText("")
        self.HomeSidebar.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.BukuSidebar.setText(QCoreApplication.translate("MainWindow", u"Daftar Buku", None))
        self.AnggotaSidebar.setText(QCoreApplication.translate("MainWindow", u"Daftar Anggota", None))
        self.inputSearch.setText("")
        self.inputSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cari Judul Buku, Penulis, Anggota", None))
        self.buttonSearch.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nama", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Alamat Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"No Telepon", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.AddButton.setText("")
    # retranslateUi

