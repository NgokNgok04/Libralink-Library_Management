from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from components.Header import Header
from components.Sidebar import Sidebar
from components.AddButton import AddButton
from components.DaftarAnggotaPage import DaftarAnggotaPage
from components.DaftarPeminjaman import DaftarPeminjaman
from components.DaftarBukuPage import DaftarBukuPage
from components.DeleteConfirmationForm import DeleteConfirmationForm
from components.FormAnggota import FormAnggota
from components.FormBuku import FormBuku

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("LibraLink Management")
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        print(screenSize)
        self.resize(screenSize.width(), screenSize.height())
        self.setMinimumSize(QSize(screenSize.width(), screenSize.height()))
        self.setMaximumSize(QSize(screenSize.width(), screenSize.height()))
        self.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.headerWidget = Header(self.centralwidget)
        self.sidebarWidget = Sidebar(self.centralwidget)

        self.sidebarWidget.showWidget.connect(self.headerWidget.changeStackedWidgetIndex)
        
        # page Daftar Anggota and Daftar Buku
        self.stackedWidgetPage = QStackedWidget(self.centralwidget)
        self.stackedWidgetPage.setGeometry(QRect(360, 178, screenSize.width() - 355, screenSize.height() - 240))
        # self.stackedWidgetPage.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.HomePage = QWidget()
        self.Daftar_BukuPage = DaftarBukuPage()
        self.Daftar_AnggotaPage = DaftarAnggotaPage()

        self.stackedWidgetPage.addWidget(self.HomePage)
        self.stackedWidgetPage.addWidget(self.Daftar_BukuPage)
        self.stackedWidgetPage.addWidget(self.Daftar_AnggotaPage)
        self.stackedWidgetPage.setCurrentIndex(0)

        self.headerWidget.setContentsMargins(0, 0, 0, 0)
        self.addButton = AddButton(self.centralwidget,clicked = lambda: self.showAddForm(self.stackedWidgetPage.currentIndex(),True))
        self.addButton.setGeometry(QRect(screenSize.width() - 80, screenSize.height() - 105, 70, 70))
        self.addButton.hide()
        self.headerWidget.showAddButton.connect(self.addButton.isShowAddButton)
        self.headerWidget.showPageIndex.connect(self.whatPageToShow)

        self.DaftarPeminjaman = DaftarPeminjaman(self.centralwidget)
        self.DaftarPeminjaman.hide()
        self.DaftarPeminjaman.showDaftarPeminjaman.connect(self.IsShowDaftarPeminjaman)
        self.Daftar_AnggotaPage.showDaftarPeminjaman.connect(self.IsShowDaftarPeminjaman)
        

        # self.deleteConfirmationFormBuku = DeleteConfirmationForm(self.centralwidget)
        # self.deleteConfirmationFormBuku.title.setText("Apakah anda yakin\ningin menghapus buku ini?")
        # self.deleteConfirmationFormAnggota = DeleteConfirmationForm(self.centralwidget)
        # self.deleteConfirmationFormAnggota.title.setText("Apakah anda yakin\ningin menghapus anggota ini?")
        # self.deleteConfirmationFormBuku.hide()
        # self.deleteConfirmationFormAnggota.hide()
        # self.deleteConfirmationFormAnggota.confirmDeleteSignal.connect(self.Daftar_AnggotaPage.confirmDeletion)
        # self.deleteConfirmationFormAnggota.showConfirmDelete.connect(self.showDeleteConfirmationFormAnggota)
        # self.deleteConfirmationFormBuku.showConfirmDelete.connect(self.showDeleteConfirmationFormBuku)
        # self.Daftar_AnggotaPage.showConfirmDelete.connect(self.showDeleteConfirmationFormAnggota)
        # self.Daftar_BukuPage.showConfirmDelete.connect(self.showDeleteConfirmationFormBuku)

        self.deleteConfirmationFormAnggota = DeleteConfirmationForm(self.centralwidget)
        self.deleteConfirmationFormAnggota.title.setText("Apakah anda yakin\ningin menghapus anggota ini?")
        self.deleteConfirmationFormAnggota.hide()
        self.deleteConfirmationFormAnggota.confirmDeleteSignal.connect(self.Daftar_AnggotaPage.confirmDeletion)
        self.deleteConfirmationFormAnggota.showConfirmDelete.connect(self.showDeleteConfirmationFormAnggota)
        self.Daftar_AnggotaPage.showConfirmDelete.connect(self.showDeleteConfirmationFormAnggota)

        self.deleteConfirmationFormBuku = DeleteConfirmationForm(self.centralwidget)
        self.deleteConfirmationFormBuku.title.setText("Apakah anda yakin\ningin menghapus buku ini?")
        self.deleteConfirmationFormBuku.hide()
        self.deleteConfirmationFormBuku.confirmDeleteSignal.connect(self.Daftar_BukuPage.confirmDeletion)
        self.deleteConfirmationFormBuku.showConfirmDelete.connect(self.showDeleteConfirmationFormBuku)
        self.Daftar_BukuPage.showConfirmDelete.connect(self.showDeleteConfirmationFormBuku)


        # EDIT FORM BUKU
        self.editFormBuku = FormBuku(self.centralwidget, tipe="edit")
        self.editFormBuku.hide()

        self.editFormBuku.confirmEdit.connect(self.Daftar_BukuPage.confirmEdit)
        self.Daftar_BukuPage.rowEmiter.connect(self.editFormBuku.aidiPassing)
        # self.Daftar_BukuPage.rowEmiter.connect(self.editFormBuku.confirmEditClicked)
        # self.Daftar_BukuPage.typeSignal.connect(self.editFormBuku.setupUi)
        self.editFormBuku.confirmAdd.connect(self.Daftar_BukuPage.confirmAdd)

        self.editFormBuku.showEditForm.connect(self.showEditFormBuku)
        self.Daftar_BukuPage.showEditForm.connect(self.showEditFormBuku)
        self.editFormBuku.cancelButton.clicked.connect(lambda: self.showEditFormBuku(False))

        # ADD FORM
        self.addFormBuku = FormBuku(self.centralwidget, tipe="add")
        self.addFormBuku.hide()

        self.addFormBuku.confirmEdit.connect(self.Daftar_BukuPage.confirmEdit)
        self.Daftar_BukuPage.rowEmiter.connect(self.addFormBuku.aidiPassing)
        # self.Daftar_BukuPage.rowEmiter.connect(self.addFormBuku.confirmEditClicked)
        # self.Daftar_BukuPage.typeSignal.connect(self.addFormBuku.setupUi)
        self.addFormBuku.confirmAdd.connect(self.Daftar_BukuPage.confirmAdd)

        self.addFormBuku.showEditForm.connect(self.showEditFormBuku)
        self.Daftar_BukuPage.showEditForm.connect(self.showEditFormBuku)
        self.addFormBuku.cancelButton.clicked.connect(lambda: self.showEditFormBuku(False))

        # EDIT FORM ANGGOTA
        self.editFormAnggota = FormAnggota(self.centralwidget, tipe = "edit")
        self.editFormAnggota.hide()

        self.editFormAnggota.confirmEdit.connect(self.Daftar_AnggotaPage.confirmEdit)
        self.Daftar_AnggotaPage.rowEmiter.connect(self.editFormAnggota.aidiPassing)
        self.editFormAnggota.confirmAdd.connect(self.Daftar_AnggotaPage.confirmAdd)


        self.editFormAnggota.showEditForm.connect(self.showEditFormAnggota)
        self.Daftar_AnggotaPage.showEditForm.connect(self.showEditFormAnggota)
        self.editFormAnggota.cancelButton.clicked.connect(lambda: self.showEditFormAnggota(False))

        # ADD FORM ANGGOTA
        self.addFormAnggota = FormAnggota(self.centralwidget, tipe = "add")
        self.addFormAnggota.hide()

        self.addFormAnggota.confirmEdit.connect(self.Daftar_AnggotaPage.confirmEdit)
        self.Daftar_AnggotaPage.rowEmiter.connect(self.addFormAnggota.aidiPassing)
        self.addFormAnggota.confirmAdd.connect(self.Daftar_AnggotaPage.confirmAdd)


        self.addFormAnggota.showAddForm.connect(self.showAddFormAnggota)
        self.Daftar_AnggotaPage.showAddForm.connect(self.showAddFormAnggota)
        self.addFormAnggota.cancelButton.clicked.connect(lambda: self.showEditFormAnggota(False))
        # self.formBuku = FormBuku(self.centralwidget)
        # self.formAnggota = FormAnggota(self.centralwidget)
        # self.formBuku.hide()
        # self.formAnggota.hide()
        # self.formBuku.cancelButton.clicked.connect(lambda: self.showAddForm(1,False))
        # self.formAnggota.cancelButton.clicked.connect(lambda: self.showAddForm(2,False))

    @Slot(int)
    def whatPageToShow(self,index):
        self.stackedWidgetPage.setCurrentIndex(index)
        self.editFormBuku.hide()
        # self.editFormAnggota.hide()
        self.deleteConfirmationFormBuku.hide()
        self.deleteConfirmationFormAnggota.hide()
    
    @Slot(bool)
    def IsShowDaftarPeminjaman(self,isShow2):
        if(isShow2):
            self.DaftarPeminjaman.show()
        else:
            self.DaftarPeminjaman.hide()

    @Slot(bool)
    def showDeleteConfirmationFormBuku(self, isShow):
        if isShow:
            self.deleteConfirmationFormBuku.show()
        else:
            self.deleteConfirmationFormBuku.hide()

    @Slot(bool)
    def showDeleteConfirmationFormAnggota(self, isShow):
        if isShow:
            self.deleteConfirmationFormAnggota.show()
        else:
            self.deleteConfirmationFormAnggota.hide()
    
    @Slot(bool)
    def showEditFormBuku(self, isShowFB):
        if isShowFB:
            self.editFormBuku.show()
        else:
            self.editFormBuku.hide()

    @Slot(bool)
    def showEditFormAnggota(self, isShowFA):
        if isShowFA:
            self.editFormAnggota.show()
        else:
            self.editFormAnggota.hide()

    @Slot(bool)
    def showAddFormBuku(self, isShowFBA):
        if isShowFBA:
            self.addFormBuku.show()
        else:
            self.addFormBuku.hide()

    @Slot(bool)
    def showAddFormAnggota(self, isShowFAA):
        if isShowFAA:
            self.addFormAnggota.show()
        else:
            self.addFormAnggota.hide()
