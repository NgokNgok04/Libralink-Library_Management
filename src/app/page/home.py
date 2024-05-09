# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 527)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: white;\n"
"    height: 30px;\n"
"    border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/assets/profilePlaceHolder.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.home_closed = QPushButton(self.icon_only_widget)
        self.home_closed.setObjectName(u"home_closed")
        icon = QIcon()
        icon.addFile(u":/assets/homeLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_closed.setIcon(icon)
        self.home_closed.setIconSize(QSize(24, 24))
        self.home_closed.setCheckable(True)
        self.home_closed.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_closed)

        self.buku_closed = QPushButton(self.icon_only_widget)
        self.buku_closed.setObjectName(u"buku_closed")
        icon1 = QIcon()
        icon1.addFile(u":/assets/daftarBukuLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buku_closed.setIcon(icon1)
        self.buku_closed.setIconSize(QSize(24, 24))
        self.buku_closed.setCheckable(True)
        self.buku_closed.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.buku_closed)

        self.anggota_closed = QPushButton(self.icon_only_widget)
        self.anggota_closed.setObjectName(u"anggota_closed")
        icon2 = QIcon()
        icon2.addFile(u":/assets/daftarAnggotaLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.anggota_closed.setIcon(icon2)
        self.anggota_closed.setIconSize(QSize(24, 24))
        self.anggota_closed.setCheckable(True)
        self.anggota_closed.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.anggota_closed)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 280, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logout_closed = QPushButton(self.icon_only_widget)
        self.logout_closed.setObjectName(u"logout_closed")
        icon3 = QIcon()
        icon3.addFile(u":/assets/logOutLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_closed.setIcon(icon3)
        self.logout_closed.setIconSize(QSize(24, 24))
        self.logout_closed.setCheckable(True)

        self.verticalLayout_3.addWidget(self.logout_closed)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: white;\n"
"	text-align: left;\n"
"    height: 30px;\n"
"    border: none;\n"
"    padding-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #F5FAFE;\n"
"	color: #1F95EF;\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/assets/profilePlaceHolder.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.home_open = QPushButton(self.icon_name_widget)
        self.home_open.setObjectName(u"home_open")
        self.home_open.setIcon(icon)
        self.home_open.setIconSize(QSize(24, 24))
        self.home_open.setCheckable(True)
        self.home_open.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_open)

        self.buku_open = QPushButton(self.icon_name_widget)
        self.buku_open.setObjectName(u"buku_open")
        self.buku_open.setIcon(icon1)
        self.buku_open.setIconSize(QSize(24, 24))
        self.buku_open.setCheckable(True)
        self.buku_open.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.buku_open)

        self.anggota_open = QPushButton(self.icon_name_widget)
        self.anggota_open.setObjectName(u"anggota_open")
        self.anggota_open.setIcon(icon2)
        self.anggota_open.setIconSize(QSize(24, 24))
        self.anggota_open.setCheckable(True)
        self.anggota_open.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.anggota_open)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 168, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.logout_open = QPushButton(self.icon_name_widget)
        self.logout_open.setObjectName(u"logout_open")
        icon4 = QIcon()
        icon4.addFile(u"assets/logOutLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_open.setIcon(icon4)
        self.logout_open.setIconSize(QSize(24, 24))
        self.logout_open.setCheckable(True)

        self.verticalLayout_4.addWidget(self.logout_open)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border: none;")
        icon5 = QIcon()
        icon5.addFile(u":/assets/menuLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon5)
        self.menu.setCheckable(True)
        self.menu.setChecked(False)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(127, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon6 = QIcon()
        icon6.addFile(u":/assets/searchLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon6)

        self.horizontalLayout.addWidget(self.pushButton_14)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border: none;")
        icon7 = QIcon()
        icon7.addFile(u":/assets/profileLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon7)

        self.horizontalLayout_4.addWidget(self.pushButton_15)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.label_5 = QLabel(self.Home)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 170, 161, 101))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_5.setFont(font1)
        self.stackedWidget.addWidget(self.Home)
        self.daftarBuku = QWidget()
        self.daftarBuku.setObjectName(u"daftarBuku")
        self.label_4 = QLabel(self.daftarBuku)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 180, 221, 61))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.daftarBuku)
        self.daftarAnggota = QWidget()
        self.daftarAnggota.setObjectName(u"daftarAnggota")
        self.label_6 = QLabel(self.daftarAnggota)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(190, 140, 281, 121))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.daftarAnggota)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.anggota_closed.toggled.connect(self.anggota_open.setChecked)
        self.buku_closed.toggled.connect(self.buku_open.setChecked)
        self.home_closed.toggled.connect(self.home_open.setChecked)
        self.anggota_open.toggled.connect(self.anggota_closed.setChecked)
        self.buku_open.toggled.connect(self.buku_closed.setChecked)
        self.home_open.toggled.connect(self.home_closed.setChecked)
        self.logout_closed.toggled.connect(MainWindow.close)
        self.logout_open.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home_closed.setText("")
        self.buku_closed.setText("")
        self.anggota_closed.setText("")
        self.logout_closed.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.home_open.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.buku_open.setText(QCoreApplication.translate("MainWindow", u"Buku", None))
        self.anggota_open.setText(QCoreApplication.translate("MainWindow", u"Anggota", None))
        self.logout_open.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.menu.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ini Home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ini Daftar Buku", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ini Daftar Anggota", None))
    # retranslateUi

