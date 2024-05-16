from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class FormAnggota(QWidget):
    showEditForm = Signal(bool)
    showAddForm = Signal(bool)
    confirmEdit = Signal(str, str, str, bool, str)
    confirmAdd = Signal(str, str, str, bool)

    def __init__(self,parent=None, tipe = None):
        super().__init__(parent)
        self.setupUi(tipe)
        self.aidi = None
    
    def setupUi(self, tipe):
        self.setStyleSheet(u"border: none;")
        screenSize = QGuiApplication.primaryScreen().geometry()
        self.layoutFormAnggota = QWidget(self)
        x = (screenSize.width() - 480) // 2
        y = (screenSize.height() - 550) // 2
        self.layoutFormAnggota.setGeometry(QRect(0,0,480,550))
        self.move(x,y)
        self.layoutFormAnggota.setStyleSheet(u"background-color: rgb(255,255,255); border: 2px solid rgb(100, 119, 219); border-radius: 10px;")
        
        self.title = QLabel(self.layoutFormAnggota)
        self.title.setText("FORM ANGGOTA")
        self.title.setAlignment(Qt.AlignCenter)
        xTitle = (self.layoutFormAnggota.width() - 350) // 2
        print(xTitle)
        self.title.setGeometry(QRect(xTitle,50,350,41))

        fontTitle = QFont()
        fontTitle.setFamilies([u"MS Shell Dlg 2"])
        fontTitle.setPointSize(30)
        fontTitle.setBold(True)
        self.title.setFont(fontTitle)
        self.title.setStyleSheet(u"color: rgb(85,85,255); border: none;")

        self.cancelButton = QPushButton(self.layoutFormAnggota)
        self.cancelButton.setStyleSheet(u"background-color: none; border: none;")
        xCancel = self.layoutFormAnggota.width() - 30
        self.cancelButton.setGeometry(QRect(xCancel,10,20,20))
        iconCancel = QIcon()
        iconCancel.addFile(u"assets/cancel.png",QSize(),QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(iconCancel)
        self.cancelButton.setIconSize(QSize(18,18))
        self.cancelButton.setCheckable(True)
        self.cancelButton.setAutoExclusive(True)
        self.cancelButton.clicked.connect(lambda: self.showEditForm.emit(False))


        fontInput = QFont()
        fontInput.setFamilies([u"MS Shell Dlg 2"])
        fontInput.setPointSize(18)

        self.layoutIDlnput = QWidget(self.layoutFormAnggota)
        self.layoutIDlnput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutIDlnput.setGeometry(QRect(40,110,400,50))
        
        self.IDButton = QPushButton(self.layoutIDlnput)
        self.IDButton.setGeometry(QRect(0,0,50,50))
        iconID = QIcon()
        iconID.addFile(u"assets/idLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.IDButton.setIcon(iconID)
        self.IDButton.setIconSize(QSize(24,24))
        self.IDButton.setCheckable(False)
        self.IDButton.setAutoExclusive(False)
        self.IDButton.setStyleSheet(u"border: none;")

        self.IDInput = QLineEdit(self.layoutIDlnput)
        self.IDInput.setFont(fontInput)
        self.IDInput.setGeometry(QRect(40,0,350,50))
        self.IDInput.setPlaceholderText("ID Anggota")
        self.IDInput.setStyleSheet(u"color: rgb(93, 95, 239); padding-left: 10px; border: none; background-color: transparent;")

        self.layoutNamaInput = QWidget(self.layoutFormAnggota)
        self.layoutNamaInput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutNamaInput.setGeometry(QRect(40,180,400,50))
        
        self.namaButton = QPushButton(self.layoutNamaInput)
        self.namaButton.setGeometry(QRect(0,0,50,50))
        iconNama = QIcon()
        iconNama.addFile(u"assets/namaLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.namaButton.setIcon(iconNama)
        self.namaButton.setIconSize(QSize(24,24))
        self.namaButton.setCheckable(False)
        self.namaButton.setAutoExclusive(False)
        self.namaButton.setStyleSheet(u"border: none;")

        self.namaInput = QLineEdit(self.layoutNamaInput)
        self.namaInput.setFont(fontInput)
        self.namaInput.setGeometry(QRect(40,0,350,50))
        self.namaInput.setPlaceholderText("Nama Anggota")
        self.namaInput.setStyleSheet(u"color: rgb(93, 95, 239); padding-left: 10px; border: none; background-color: transparent;")

        self.layoutEmailInput = QWidget(self.layoutFormAnggota)
        self.layoutEmailInput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutEmailInput.setGeometry(QRect(40,250,400,50))

        self.emailButton = QPushButton(self.layoutEmailInput)
        self.emailButton.setGeometry(QRect(0,0,50,50))
        iconEmail = QIcon()
        iconEmail.addFile(u"assets/idLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.emailButton.setIcon(iconEmail)
        self.emailButton.setIconSize(QSize(24,24))
        self.emailButton.setCheckable(False)
        self.emailButton.setAutoExclusive(False)
        self.emailButton.setStyleSheet(u"border: none;")

        self.emailInput = QLineEdit(self.layoutEmailInput)
        self.emailInput.setFont(fontInput)
        self.emailInput.setGeometry(QRect(50,0,350,50))
        self.emailInput.setPlaceholderText("Alamat E-mail")
        self.emailInput.setStyleSheet(u"color: rgba(93, 95, 239, 1); border: none; background-color: transparent;")

        self.layoutTeleponInput = QWidget(self.layoutFormAnggota)
        self.layoutTeleponInput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutTeleponInput.setGeometry(QRect(40,320,400,50))

        self.teleponButton = QPushButton(self.layoutTeleponInput)
        self.teleponButton.setGeometry(QRect(0,0,50,50))
        iconTelepon = QIcon()
        iconTelepon.addFile(u"assets/kodeLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.teleponButton.setIcon(iconTelepon)
        self.teleponButton.setIconSize(QSize(24,24))
        self.teleponButton.setCheckable(False)
        self.teleponButton.setAutoExclusive(False)
        self.teleponButton.setStyleSheet(u"border: none;")

        self.teleponInput = QLineEdit(self.layoutTeleponInput)
        self.teleponInput.setFont(fontInput)
        self.teleponInput.setGeometry(QRect(50,0,350,50))
        self.teleponInput.setPlaceholderText("Nomor Telepon")
        self.teleponInput.setStyleSheet(u"color: rgba(93, 95, 239, 1); border: none; background-color: transparent;")

        self.layoutStatusButton = QWidget(self.layoutFormAnggota)
        xStatus = (self.layoutFormAnggota.width() - 250) // 2
        yStatus = 370 + (self.layoutFormAnggota.height() - 490) // 2
        self.layoutStatusButton.setGeometry(QRect(xStatus,yStatus,250,50))
        self.layoutStatusButton.setStyleSheet(u"background-color: #6477DB;")

        widthStatusButton = (self.layoutStatusButton.width() - 10) // 2
        fontStatus = fontInput
        fontStatus.setPointSize(16)
        fontStatus.setBold(True)


        self.aktifButton = QPushButton(self.layoutStatusButton, clicked = lambda: self.handleToggle(False))
        self.aktifButton.setText("Aktif")
        self.aktifButton.setStyleSheet(U"background-color: transparent; color: white; border-radius: 10px;")
        self.aktifButton.setFont(fontStatus)
        self.aktifButton.setGeometry(QRect(5,5,widthStatusButton,40))
        self.aktifButton.setCheckable(True)
        self.aktifButton.setAutoExclusive(True)
        self.aktifButton.setChecked(False)

        self.nonaktifButton = QPushButton(self.layoutStatusButton, clicked = lambda: self.handleToggle(True))
        self.nonaktifButton.setText("Nonaktif")
        self.nonaktifButton.setStyleSheet(u"background-color: white; color: #6477DB; border-radius: 10px;")
        self.nonaktifButton.setFont(fontStatus)
        self.nonaktifButton.setGeometry(QRect(widthStatusButton + 5, 5, widthStatusButton, 40))
        self.nonaktifButton.setCheckable(True)
        self.nonaktifButton.setAutoExclusive(True)
        self.nonaktifButton.setChecked(True)

        # self.aktifInput = self.aktifButton.isChecked()
        # print(self.aktifInput)

        self.simpanButton = QPushButton(self.layoutFormAnggota)
        self.simpanButton.setText("SIMPAN")
        self.simpanButton.setCheckable(True)
        fontSimpan = fontTitle
        fontSimpan.setPointSize(20)
        self.simpanButton.setFont(fontSimpan)
        self.simpanButton.setGeometry(QRect(50,self.layoutFormAnggota.height() - 70,400,50))
        self.simpanButton.setStyleSheet(u"color: white; background-color: #5D5FEF;")
        # self.simpanButton.clicked.connect(self.confirmEditClicked)
        if tipe == "edit":
            self.simpanButton.clicked.connect(self.confirmEditClicked)
        else:
            self.simpanButton.clicked.connect(self.confirmAddClicked)
    
    @Slot(str)
    def aidiPassing(self, hoho):
        print(hoho)
        self.aidi = hoho
    
    def handleToggle(self,isNonAktif):
        if(isNonAktif):
            self.aktifButton.setStyleSheet(U"background-color: transparent; color: white; border-radius: 10px;")
            self.nonaktifButton.setStyleSheet(u"background-color: white; color: #6477DB; border-radius: 10px;")
        else:
            self.nonaktifButton.setStyleSheet(U"background-color: transparent; color: white; border-radius: 10px;")
            self.aktifButton.setStyleSheet(u"background-color: white; color: #6477DB; border-radius: 10px;")
    
    def confirmEditClicked(self):
        # Emit the signal with the necessary data
        self.aktifInput = self.aktifButton.isChecked()
        self.confirmEdit.emit(self.namaInput.text(), self.emailInput.text(), self.teleponInput.text(), not self.aktifInput, self.aidi)
        self.showEditForm.emit(False)
    
    def confirmAddClicked(self):
        self.aktifInput = self.aktifButton.isChecked()
        self.confirmAdd.emit(self.namaInput.text(), self.emailInput.text(), self.teleponInput.text(), not self.aktifInput)
        self.showEditForm.emit(False)
        self.showAddForm.emit(False)