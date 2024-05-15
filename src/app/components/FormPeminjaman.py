from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sqlite3

class FormPeminjaman(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet(u"border: none;")
        screenSize = QGuiApplication.primaryScreen().geometry()
        self.layoutFormPeminjaman = QWidget(self)
        x = (screenSize.width() - 480) // 2
        y = (screenSize.height() - 550) // 2
        self.layoutFormPeminjaman.setGeometry(QRect(0,0,480,550))
        self.move(x,y)
        self.layoutFormPeminjaman.setStyleSheet(u"background-color: rgb(255,255,255); border: 2px solid rgb(100, 119, 219); border-radius: 10px;")
        
        self.title = QLabel(self.layoutFormPeminjaman)
        self.title.setText("FORM PEMINJAMAN")
        self.title.setAlignment(Qt.AlignCenter)
        xTitle = (self.layoutFormPeminjaman.width() - 410) // 2
        print(xTitle)
        self.title.setGeometry(QRect(xTitle,50,410,41))

        fontTitle = QFont()
        fontTitle.setFamilies([u"MS Shell Dlg 2"])
        fontTitle.setPointSize(30)
        fontTitle.setBold(True)
        self.title.setFont(fontTitle)
        self.title.setStyleSheet(u"color: rgb(85,85,255); border: none;")

        self.cancelButton = QPushButton(self.layoutFormPeminjaman)
        self.cancelButton.setStyleSheet(u"background-color: none; border: none;")
        xCancel = self.layoutFormPeminjaman.width() - 30
        self.cancelButton.setGeometry(QRect(xCancel,10,20,20))
        iconCancel = QIcon()
        iconCancel.addFile(u"assets/cancel.png",QSize(),QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(iconCancel)
        self.cancelButton.setIconSize(QSize(18,18))
        self.cancelButton.setCheckable(True)
        self.cancelButton.setAutoExclusive(True)
        self.cancelButton.clicked.connect(lambda: self.hideForm.emit(False))


        fontInput = QFont()
        fontInput.setFamilies([u"MS Shell Dlg 2"])
        fontInput.setPointSize(18)

        self.layoutIDAnggotalnput = QWidget(self.layoutFormPeminjaman)
        self.layoutIDAnggotalnput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutIDAnggotalnput.setGeometry(QRect(40,110,400,50))
        
        self.IDAnggota = QPushButton(self.layoutIDAnggotalnput)
        self.IDAnggota.setGeometry(QRect(0,0,50,50))
        iconIDAnggota = QIcon()
        iconIDAnggota.addFile(u"assets/namaLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IDAnggota.setIcon(iconIDAnggota)
        self.IDAnggota.setIconSize(QSize(24,24))
        self.IDAnggota.setCheckable(False)
        self.IDAnggota.setAutoExclusive(False)
        self.IDAnggota.setStyleSheet(u"border: none;")

        self.IDAnggotaInput = QLineEdit(self.layoutIDAnggotalnput)
        self.IDAnggotaInput.setFont(fontInput)
        self.IDAnggotaInput.setGeometry(QRect(40,0,350,50))
        self.IDAnggotaInput.setPlaceholderText("ID Anggota")
        self.IDAnggotaInput.setStyleSheet(u"color: rgb(93, 95, 239); padding-left: 10px; border: none; background-color: transparent;")

        self.layoutIDBukuInput = QWidget(self.layoutFormPeminjaman)
        self.layoutIDBukuInput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutIDBukuInput.setGeometry(QRect(40,180,400,50))
        
        self.IDBukuButton = QPushButton(self.layoutIDBukuInput)
        self.IDBukuButton.setGeometry(QRect(0,0,50,50))
        iconIDBuku = QIcon()
        iconIDBuku.addFile(u"assets/coverLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IDBukuButton.setIcon(iconIDBuku)
        self.IDBukuButton.setIconSize(QSize(24,24))
        self.IDBukuButton.setCheckable(False)
        self.IDBukuButton.setAutoExclusive(False)
        self.IDBukuButton.setStyleSheet(u"border: none;")

        self.IDBukuInput = QLineEdit(self.layoutIDBukuInput)
        self.IDBukuInput.setFont(fontInput)
        self.IDBukuInput.setGeometry(QRect(40,0,350,50))
        self.IDBukuInput.setPlaceholderText("ID Buku")
        self.IDBukuInput.setStyleSheet(u"color: rgb(93, 95, 239); padding-left: 10px; border: none; background-color: transparent;")
  
        self.layoutPinjamBukuInput = QWidget(self.layoutFormPeminjaman)
        self.layoutPinjamBukuInput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutPinjamBukuInput.setGeometry(QRect(40,250,400,50))
        
        self.pinjamButton = QPushButton(self.layoutPinjamBukuInput)
        self.pinjamButton.setGeometry(QRect(0,0,50,50))
        pinjamBuku = QIcon()
        pinjamBuku.addFile(u"assets/tglPinjamLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pinjamButton.setIcon(pinjamBuku)
        self.pinjamButton.setIconSize(QSize(24,24))
        self.pinjamButton.setCheckable(False)
        self.pinjamButton.setAutoExclusive(False)
        self.pinjamButton.setStyleSheet(u"border: none;")

        self.pinjamInput = QDateEdit(self.layoutPinjamBukuInput)
        self.pinjamInput.setCalendarPopup(True)
        self.pinjamInput.setDate(QDate.currentDate())
        self.pinjamInput.setFont(fontInput)
        self.pinjamInput.setGeometry(QRect(40,0,350,50))
        self.layoutKembalianBukuInput = QWidget(self.layoutFormPeminjaman)
        self.layoutKembalianBukuInput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutKembalianBukuInput.setGeometry(QRect(40,320,400,50))
        
        self.kembalianButton = QPushButton(self.layoutKembalianBukuInput)
        self.kembalianButton.setGeometry(QRect(0,0,50,50))
        kembalianBuku = QIcon()
        kembalianBuku.addFile(u"assets/tglPengembalianLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.kembalianButton.setIcon(kembalianBuku)
        self.kembalianButton.setIconSize(QSize(24,24))
        self.kembalianButton.setCheckable(False)
        self.kembalianButton.setAutoExclusive(False)
        self.kembalianButton.setStyleSheet(u"border: none;")

        self.kembalianInput = QDateEdit(self.layoutKembalianBukuInput)
        self.kembalianInput.setCalendarPopup(True)
        self.kembalianInput.setDate(QDate.currentDate())
        self.kembalianInput.setFont(fontInput)
        self.kembalianInput.setGeometry(QRect(40,0,350,50))
        # self.kembalianInput.setStyleSheet(u"color: rgb(93, 95, 239); padding-left: 10px; border: none; background-color: transparent;")
                # Customize the appearance of the QDateEdit
        self.kembalianInput.setStyleSheet("""
            QDateEdit {
                border: none;
                color: rgb(93, 95, 239);
                background-color: transparent;
            }
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                border: none;
            }
            QDateEdit::down-arrow {
                image: url(./assets/dropdownLogo.png);
                width: 18px;
                height: 18px;
            }
            QCalendarWidget {
                border: 1px solid rgb(218, 218, 218);
                border-radius: 5px;
                background-color: white;
            }
            QCalendarWidget QToolButton {
                color: white;
                border: none;
                background-color: transparent;
            }
            QCalendarWidget QToolButton::menu-indicator {
                image: none;  /* Hide the dropdown icon */
            }
            QCalendarWidget QToolButton::hover {
                background-color: rgb(80, 99, 199);
            }
            QCalendarWidget QToolButton::pressed {
                background-color: rgb(60, 79, 179);
            }
            QCalendarWidget QMenu {
                background-color: white;
                border: 1px solid rgb(218, 218, 218);
                color: rgb(93, 95, 239);
            }
            QCalendarWidget QSpinBox {
                background-color: white;
                color: none;
            }
            QCalendarWidget QTableView {
                background-color: white;
                border: 1px solid rgb(218, 218, 218);
                color: rgb(0, 0, 0);
            }
            QCalendarWidget QTableView QHeaderView::section {
                background-color: white;
                color: rgb(255, 255, 255);
                font-weight: bold;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: rgb(218, 218, 218);
            }
        """)

        self.pinjamInput.setStyleSheet("""
            QDateEdit {
                border: none;
                color: rgb(93, 95, 239);
                background-color: transparent;
            }
            QDateEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                border: none;
            }
            QDateEdit::down-arrow {
                image: url(./assets/dropdownLogo.png);
                width: 18px;
                height: 18px;
            }
            QCalendarWidget {
                border: 1px solid rgb(218, 218, 218);
                border-radius: 5px;
                background-color: white;
            }
            QCalendarWidget QToolButton {
                color: white;
                border: none;
                background-color: transparent;
            }
            QCalendarWidget QToolButton::menu-indicator {
                image: none;  /* Hide the dropdown icon */
            }
            QCalendarWidget QToolButton::hover {
                background-color: rgb(80, 99, 199);
            }
            QCalendarWidget QToolButton::pressed {
                background-color: rgb(60, 79, 179);
            }
            QCalendarWidget QMenu {
                background-color: white;
                border: 1px solid rgb(218, 218, 218);
                color: rgb(93, 95, 239);
            }
            QCalendarWidget QSpinBox {
                background-color: white;
                color: none;
            }
            QCalendarWidget QTableView {
                background-color: white;
                border: 1px solid rgb(218, 218, 218);
                color: rgb(0, 0, 0);
            }
            QCalendarWidget QTableView QHeaderView::section {
                background-color: white;
                color: rgb(255, 255, 255);
                font-weight: bold;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: rgb(218, 218, 218);
            }
        """)

        self.simpanButton = QPushButton(self.layoutFormPeminjaman)
        self.simpanButton.setText("SIMPAN")
        fontSimpan = fontTitle
        fontSimpan.setPointSize(20)
        self.simpanButton.setFont(fontSimpan)
        self.simpanButton.setGeometry(QRect(50,self.layoutFormPeminjaman.height() - 70,400,50))
        self.simpanButton.setStyleSheet(u"color: white; background-color: #5D5FEF;")
        