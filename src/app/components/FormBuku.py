from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
import shutil
import sqlite3
class FormBuku(QWidget):
    showEditForm = Signal(bool)
    showAddForm = Signal(bool)
    confirmEdit = Signal(str, str, str, str)
    confirmAdd = Signal(str, str, str)
    rowReciever = Signal(str)
    typeReceiver = Signal(str)

    def __init__(self, parent = None, tipe = None):
        super().__init__(parent)
        self.setupUi(tipe)
        self.aidi = None
    
    def setupUi(self, tipe):
        self.fileName = ""
        # self.aidi = 1
        # self.aidi = self.giveId()
        self.setStyleSheet(u"border: none;")
        screenSize = QGuiApplication.primaryScreen().geometry()
        self.layoutFormBuku = QWidget(self)
        x = (screenSize.width() - 508) // 2
        y = (screenSize.height() - 550) // 2
        self.layoutFormBuku.setGeometry(QRect(0,0,480,550))
        self.move(x,y)
        self.layoutFormBuku.setStyleSheet(u"background-color: rgb(255,255,255); border: 2px solid rgb(100, 119, 219); border-radius: 10px;")
        
        self.title = QLabel(self.layoutFormBuku)
        self.title.setText("FORM BUKU")
        self.title.setAlignment(Qt.AlignCenter)
        xTitle = (self.layoutFormBuku.width() - 240) // 2
        print(xTitle)
        self.title.setGeometry(QRect(xTitle,50,240,41))
        # self.title.setStyleSheet(u"background-color: rgb(255,255,0);")

        # DATA +====================================
        

        fontTitle = QFont()
        fontTitle.setFamilies([u"MS Shell Dlg 2"])
        fontTitle.setPointSize(30)
        fontTitle.setBold(True)
        self.title.setFont(fontTitle)
        self.title.setStyleSheet(u"color: rgb(85,85,255); border: none;")

        self.cancelButton = QPushButton(self.layoutFormBuku)
        self.cancelButton.setStyleSheet(u"background-color: none; border: none;")
        xCancel = self.layoutFormBuku.width() - 30
        self.cancelButton.setGeometry(QRect(xCancel,10,20,20))
        iconCancel = QIcon()
        iconCancel.addFile(u"assets/cancel.png",QSize(),QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(iconCancel)
        self.cancelButton.setIconSize(QSize(18,18))
        self.cancelButton.setCheckable(True)
        self.cancelButton.setAutoExclusive(True)
        self.cancelButton.clicked.connect(lambda: self.showEditForm.emit(False))
        self.cancelButton.clicked.connect(lambda: self.showAddForm.emit(False))

        fontInput = QFont()
        fontInput.setFamilies([u"MS Shell Dlg 2"])
        fontInput.setPointSize(18)

        self.layoutJudulnput = QWidget(self.layoutFormBuku)
        self.layoutJudulnput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutJudulnput.setGeometry(QRect(40,110,400,50))
        
        self.judulButton = QPushButton(self.layoutJudulnput)
        self.judulButton.setGeometry(QRect(0,0,50,50))
        iconJudul = QIcon()
        iconJudul.addFile(u"assets/judulLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.judulButton.setIcon(iconJudul)
        self.judulButton.setIconSize(QSize(24,24))
        self.judulButton.setCheckable(False)
        self.judulButton.setAutoExclusive(False)
        self.judulButton.setStyleSheet(u"border: none;")

        self.judulInput = QLineEdit(self.layoutJudulnput)
        self.judulInput.setFont(fontInput)
        self.judulInput.setGeometry(QRect(40,0,350,50))
        self.judulInput.setPlaceholderText("Judul Buku")
        self.judulInput.setStyleSheet(u"color: rgb(93, 95, 239); padding-left: 10px; border: none; background-color: transparent;")

        self.layoutKodeinput = QWidget(self.layoutFormBuku)
        self.layoutKodeinput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutKodeinput.setGeometry(QRect(40,180,400,50))
        
        self.kodeButton = QPushButton(self.layoutKodeinput)
        self.kodeButton.setGeometry(QRect(0,0,50,50))
        iconkode = QIcon()
        iconkode.addFile(u"assets/kodeLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.kodeButton.setIcon(iconkode)
        self.kodeButton.setIconSize(QSize(24,24))
        self.kodeButton.setCheckable(False)
        self.kodeButton.setAutoExclusive(False)
        self.kodeButton.setStyleSheet(u"border: none;")

        self.kodeInput = QLineEdit(self.layoutKodeinput)
        self.kodeInput.setFont(fontInput)
        self.kodeInput.setGeometry(QRect(40,0,350,50))
        self.kodeInput.setPlaceholderText("Kode Buku")
        
        self.kodeInput.setStyleSheet(u"color: rgb(93, 95, 239); padding-left: 10px; border: none; background-color: transparent;")

        self.layoutCoverInput = QWidget(self.layoutFormBuku)
        self.layoutCoverInput.setStyleSheet(u"background-color: none; border: 2px solid rgb(218, 218, 218); ")
        self.layoutCoverInput.setGeometry(QRect(40,250,400,50))

        self.coverButton = QPushButton(self.layoutCoverInput)
        self.coverButton.setGeometry(QRect(0,0,50,50))
        iconCover = QIcon()
        iconCover.addFile(u"assets/coverLogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.coverButton.setIcon(iconCover)
        self.coverButton.setIconSize(QSize(24,24))
        self.coverButton.setCheckable(False)
        self.coverButton.setAutoExclusive(False)
        self.coverButton.setStyleSheet(u"border: none;")

        self.coverInput = QLabel(self.layoutCoverInput)
        self.coverInput.setText("Cover Buku")
        self.coverInput.setFont(fontInput)
        self.coverInput.setGeometry(QRect(50,0,250,50))
        self.coverInput.setStyleSheet(u"color: rgba(93, 95, 239, 128); border: none; background-color: transparent;")

        self.coverUpload = QPushButton(self.layoutCoverInput)
        fontUpload = fontInput
        fontUpload.setPointSize(12)
        self.coverUpload.setFont(fontInput)
        self.coverUpload.setText("Unggah Gambar")
        self.coverUpload.setGeometry(QRect(265,5,130,40))
        self.coverUpload.setStyleSheet(u"color: white; background-color: #828282; border:none; padding: 5px;")
        self.coverUpload.clicked.connect(self.uploadImage)

        self.simpanButton = QPushButton(self.layoutFormBuku)
        self.simpanButton.setText("SIMPAN")
        self.simpanButton.setCheckable(True)
        fontSimpan = fontTitle
        fontSimpan.setPointSize(20)
        self.simpanButton.setFont(fontSimpan)
        self.simpanButton.setGeometry(QRect(40,self.layoutFormBuku.height() - 70,400,50))
        self.simpanButton.setStyleSheet(u"color: white; background-color: #5D5FEF;")
        if tipe == "edit":
            self.simpanButton.clicked.connect(self.confirmEditClicked)
        else:
            self.simpanButton.clicked.connect(self.confirmAddClicked)

    @Slot(str)
    def aidiPassing(self, hoho):
        print(hoho)
        self.aidi = hoho

        conn = sqlite3.connect('datarpl.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT judul FROM buku WHERE buku_id = ?", (self.aidi,))
        result = cursor.fetchone()
        self.judulInput.setText(result[0])

        cursor.execute("SELECT isbn FROM buku WHERE buku_id = ?", (self.aidi,))
        result = cursor.fetchone()
        self.kodeInput.setText(result[0])
    
    def giveId(self):
        return self.aidi

    def uploadImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Image", "", "Image Files (*.png)")
        if fileName:
            self.coverUpload.setText("Unggah Berhasil!")
            self.coverUpload.setStyleSheet(u"color: white; background-color: #6FCF97; border: none; padding: 5px;")
            self.saveImageToAssets(fileName)
            self.fileName = fileName



    def saveImageToAssets(self, sourcePath):
        destFolder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets/coverBukuCollection')
        if not os.path.exists(destFolder):
            os.makedirs(destFolder)

        fileName = os.path.basename(sourcePath)
        destPath = os.path.join(destFolder, fileName)

        if os.path.exists(destPath):
            print(f"File '{fileName}' already exists in the destination folder. Skipping...")
            return

        shutil.copy(sourcePath, destPath)

    def confirmEditClicked(self, aidi):
        # Emit the signal with the necessary data
        # aidi = self.aidiPassing()
        tempName = extractName(self.fileName)
        self.confirmEdit.emit(self.judulInput.text(), self.kodeInput.text(),"./assets/coverBukuCollection/" + tempName, self.aidi)
        self.showEditForm.emit(False)
        self.showAddForm.emit(False)
    
    def confirmAddClicked(self):
        tempName = extractName(self.fileName)
        self.confirmAdd.emit(self.judulInput.text(), self.kodeInput.text(), "./assets/coverBukuCollection/" + tempName)
        self.showEditForm.emit(False)
        self.showAddForm.emit(False)
    
def extractName(url):
    last_slash_index = url.rfind('/')
    if last_slash_index != -1:
        return url[last_slash_index + 1:]
    else:
        return url