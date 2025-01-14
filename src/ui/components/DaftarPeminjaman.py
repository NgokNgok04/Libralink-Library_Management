from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
from ui.components.AddButton import AddButton
from controller.peminjaman_controller import Peminjaman_Controller

icons_folder = os.path.join(os.path.dirname(__file__), '../../../assets/icons')
os.makedirs(icons_folder, exist_ok=True)

class Peminjaman:
    def __init__(self,anggota_id,buku_id,tanggal_pinjam,tanggal_pengembalian):
        self.anggota_id = anggota_id
        self.buku_id = buku_id
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_pengembalian = tanggal_pengembalian
    
    def addTitle(self,title):
        self.title = title

class DaftarPeminjaman(QWidget):
    doReload = Signal(bool)
    showDaftarPeminjaman = Signal(bool)
    showConfirmDelete = Signal(bool)
    showFormPeminjaman = Signal(bool)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        self.peminjaman_controller = Peminjaman_Controller()
        screenSize = QGuiApplication.primaryScreen().geometry()
        self.layoutDaftarPeminjaman = QWidget(self)
        x = (screenSize.width() - 700) // 2
        y = (screenSize.height() - 318) // 2
        self.layoutDaftarPeminjaman.setGeometry(0,0,700,318)
        self.move(x,y)

        self.setStyleSheet(u"border: none;")

        self.layoutDaftarPeminjaman.setStyleSheet(u"background-color: white; border: 1px solid rgb(109, 141, 223); border-radius: 14px")
        self.title = QLabel(self)
        self.title.setText("Buku yang dipinjam")
        self.title.setGeometry(QRect(190, 10, 350, 55))

        font = QFont()
        font.setFamilies([u"DubaiMedium"])
        font.setPointSize(22)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: rgb(93, 95, 239);")
        self.title.setAlignment(Qt.AlignCenter)

        self.cancelButton = QPushButton(self.layoutDaftarPeminjaman)
        self.cancelButton.setStyleSheet(u"QPushButton{background-color: none; border: none;} QPushButton::hover{background-color: rgba(227, 233, 255, 191);}")
        self.cancelButton.setGeometry(QRect(670,10,20,20))
        iconCancel = QIcon()

        iconcancelLogo_path = os.path.join(icons_folder, 'cancel.png')
        iconCancel.addFile(iconcancelLogo_path,QSize(),QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(iconCancel)
        self.cancelButton.setIconSize(QSize(18,18))
        self.cancelButton.setCheckable(True)
        self.cancelButton.setAutoExclusive(True)
        self.cancelButton.clicked.connect(lambda: self.showDaftarPeminjaman.emit(False))

        self.tableWidget = QTableWidget(self)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)

        idHeader = QTableWidgetItem()
        judulHeader = QTableWidgetItem()
        tglPinjam = QTableWidgetItem()
        tglKembali = QTableWidgetItem()
        actionHeader = QTableWidgetItem()
        idHeader.setText("ID Buku")
        judulHeader.setText("Judul Buku")
        tglPinjam.setText("Tanggal Pinjam")
        tglKembali.setText("Tanggal Pengembalian")
        self.tableWidget.setHorizontalHeaderItem(0, idHeader)
        self.tableWidget.setHorizontalHeaderItem(1, judulHeader)
        self.tableWidget.setHorizontalHeaderItem(2, tglPinjam)
        self.tableWidget.setHorizontalHeaderItem(3, tglKembali)
        self.tableWidget.setHorizontalHeaderItem(4, actionHeader)

        self.tableWidget.setGeometry(QRect(10, 80, 681, 200))

        font = QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
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
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	color: rgb(130, 130, 130);\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	text-align: center;\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}    ")
        
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,280)
        self.tableWidget.setColumnWidth(2,120)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,50)

        self.addButton = AddButton(self.layoutDaftarPeminjaman)
        self.addButton.setChecked(True)
        self.addButton.setGeometry(QRect(640,260,50,50))
        self.addButton.setIconSize(QSize(30,30))
        self.addButton.setStyleSheet(u"border: none; border-radius: 25px; background-color: rgb(109, 141, 223); color: rgb(255, 255, 255);")
        self.addButton.clicked.connect(lambda: self.showFormPeminjaman.emit(True))

    def updateTable(self,dataPeminjaman):
        row = 0
        self.tableWidget.setRowCount(len(dataPeminjaman))
        
        for data in dataPeminjaman:
            title_book = str(data.title)[3:][:-4]
            self.tableWidget.setItem(row,0,QTableWidgetItem(str(data.buku_id)))
            self.tableWidget.setItem(row,1,QTableWidgetItem(str(title_book)))
            self.tableWidget.setItem(row,2,QTableWidgetItem(str(data.tanggal_pinjam)))
            self.tableWidget.setItem(row,3,QTableWidgetItem(str(data.tanggal_pengembalian)))

            trashButton = QPushButton(self.tableWidget.item(row,4))
            trashButton.setCheckable(True)
            trashButton.setAutoExclusive(True)
            trashButton.setStyleSheet(u"QPushButton{border: none; background-color: none;} QPushButton::hover{background-color: rgba(227, 233, 255, 191);} ")
            iconTrashButton = QIcon()
            iconTrashLogo_path = os.path.join(icons_folder, 'trashLogo.png')
            iconTrashButton.addFile(iconTrashLogo_path, QSize(), QIcon.Normal, QIcon.Off)
            trashButton.setIcon(iconTrashButton)
            trashButton.setIconSize(QSize(24, 24))
            trashButton.clicked.connect(self.handleTrashButtonClicked)
            trashButton.clicked.connect(lambda: self.showConfirmDelete.emit(True))

            self.tableWidget.setCellWidget(row,4,trashButton)
            row += 1
        
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row, 60)
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


    def handleTrashButtonClicked(self):
        button = self.sender()  # Get the sender widget (the trash button)
        if button:
            global_pos = button.mapToGlobal(button.rect().topLeft())
            table_pos = self.tableWidget.viewport().mapFromGlobal(global_pos)
            index = self.tableWidget.indexAt(table_pos)
            if index.isValid():
                row = index.row()
                id_item = self.tableWidget.item(row, 0)
                if id_item:
                    self.selectedRowId = int(id_item.text())
                    print("Selected Trash Peminjaman Row ID:", self.selectedRowId)
                else:
                    print("ID item is None")
            else:
                print("Invalid index")
        else:
            print("Sender button is None")
        
    @Slot(int)
    def loadData(self,IDToShow):
        daftar_peminjaman = self.peminjaman_controller.get_list_peminjaman(IDToShow)
        self.updateTable(daftar_peminjaman)

    
    @Slot(bool)
    def confirmDeletion(self,confirmed):
        if confirmed and self.selectedRowId is not None:
            self.loadData(self.peminjaman_controller.delete_peminjaman(self.selectedRowId))
            self.doReload.emit(True)