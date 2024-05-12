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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 1000)
        MainWindow.setMinimumSize(QSize(1440, 500))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
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
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.logoTitle.setFont(font)
        self.logoTitle.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.HLayoutLogo.addWidget(self.logoTitle)

        self.stackedWidgetDirectory = QStackedWidget(self.headerWidget)
        self.stackedWidgetDirectory.setObjectName(u"stackedWidgetDirectory")
        self.stackedWidgetDirectory.setGeometry(QRect(360, 120, 481, 61))
        self.HomeDirectory = QWidget()
        self.HomeDirectory.setObjectName(u"HomeDirectory")
        self.HomeLabel = QLabel(self.HomeDirectory)
        self.HomeLabel.setObjectName(u"HomeLabel")
        self.HomeLabel.setGeometry(QRect(10, 10, 101, 41))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.HomeLabel.setFont(font1)
        self.HomeLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.HomeDirectory)
        self.DaftarBukuDirectory = QWidget()
        self.DaftarBukuDirectory.setObjectName(u"DaftarBukuDirectory")
        self.DaftarBukuLabel = QLabel(self.DaftarBukuDirectory)
        self.DaftarBukuLabel.setObjectName(u"DaftarBukuLabel")
        self.DaftarBukuLabel.setGeometry(QRect(10, 10, 381, 41))
        self.DaftarBukuLabel.setFont(font1)
        self.DaftarBukuLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.DaftarBukuDirectory)
        self.DaftarAnggotaDirectory = QWidget()
        self.DaftarAnggotaDirectory.setObjectName(u"DaftarAnggotaDirectory")
        self.DaftarAnggotaLabel = QLabel(self.DaftarAnggotaDirectory)
        self.DaftarAnggotaLabel.setObjectName(u"DaftarAnggotaLabel")
        self.DaftarAnggotaLabel.setGeometry(QRect(10, 10, 431, 41))
        self.DaftarAnggotaLabel.setFont(font1)
        self.DaftarAnggotaLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.DaftarAnggotaDirectory)
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
        self.AnggotaSidebar_3 = QPushButton(self.sidebarWidget)
        self.AnggotaSidebar_3.setObjectName(u"AnggotaSidebar_3")
        self.AnggotaSidebar_3.setGeometry(QRect(30, 470, 171, 101))
        self.AnggotaSidebar_3.setFont(font)
        self.AnggotaSidebar_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 20px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-radius: 20px;\n"
"	\n"
"	background-color: rgb(109, 141, 223);\n"
"}\n"
"QPushButton:checked {\n"
"	\n"
"	color: rgb(100, 119, 219);\n"
"	background-color: rgba(227, 233, 255, 191);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets/homeLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AnggotaSidebar_3.setIcon(icon4)
        self.AnggotaSidebar_3.setIconSize(QSize(40, 40))
        self.AnggotaSidebar_3.setCheckable(True)
        self.AnggotaSidebar_3.setAutoExclusive(True)
        self.AddButton = QPushButton(self.sidebarWidget)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(130, 580, 70, 70))
        self.AddButton.setStyleSheet(u"QPushButton{\n"
"	border: none;	\n"
"	border-radius: 35px;\n"
"	\n"
"	background-color: rgb(109, 141, 223);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/assets/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddButton.setIcon(icon5)
        self.AddButton.setIconSize(QSize(34, 34))
        self.AddButton.setCheckable(True)
        self.AddButton.setAutoExclusive(False)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(370, 190, 1061, 371))
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
        self.SearchBar.setGeometry(QRect(520, 0, 541, 41))
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
        icon6 = QIcon()
        icon6.addFile(u":/assets/searchFaceLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSearch.setIcon(icon6)
        self.buttonSearch.setIconSize(QSize(24, 24))
        self.tableWidget = QTableWidget(self.Daftar_Anggota)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 50, 1021, 192))
        self.tableWidget.setMinimumSize(QSize(1021, 192))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	color: rgb(130, 130, 130);\n"
"	margin-right: 10px;\n"
"	border: none;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget{\n"
"	text-align: center;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(153)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.Daftar_Anggota)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(530, 570, 120, 80))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.AddButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logoLibraLink.setText("")
        self.logoTitle.setText(QCoreApplication.translate("MainWindow", u"Libralink Management", None))
        self.HomeLabel.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.DaftarBukuLabel.setText(QCoreApplication.translate("MainWindow", u"Daftar Buku Perpustakaan", None))
        self.DaftarAnggotaLabel.setText(QCoreApplication.translate("MainWindow", u"Daftar Anggota Perpustakaans", None))
        self.profileName.setText(QCoreApplication.translate("MainWindow", u"Muhammad Zains", None))
        self.admistrator.setText(QCoreApplication.translate("MainWindow", u"Administrator", None))
        self.profileImage.setText("")
        self.HomeSidebar.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.BukuSidebar.setText(QCoreApplication.translate("MainWindow", u"Daftar Buku", None))
        self.AnggotaSidebar.setText(QCoreApplication.translate("MainWindow", u"Daftar Anggota", None))
        self.AnggotaSidebar_3.setText("")
        self.AddButton.setText("")
        self.inputSearch.setText("")
        self.inputSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cari Judul Buku, Penulis, Anggota", None))
        self.buttonSearch.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID Anggota", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nama", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Alamat Email", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"No Telepon", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"13522093", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Matthew", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"vladimirmatthew791", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"085261138911", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Active", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

