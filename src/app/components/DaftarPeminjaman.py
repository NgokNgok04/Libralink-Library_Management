from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sqlite3
from components.AddButton import AddButton

class Peminjaman:
    def __init__(self,anggota_id,buku_id,tanggal_pinjam,tanggal_pengembalian):
        self.anggota_id = anggota_id
        self.buku_id = buku_id
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_pengembalian = tanggal_pengembalian
    
    def addTitle(self,title):
        self.title = title

class DaftarPeminjaman(QWidget):
    showDaftarPeminjaman = Signal(bool)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
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
        iconCancel.addFile(u"assets/cancel.png",QSize(),QIcon.Normal, QIcon.Off)
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
        self.addButton.setGeometry(QRect(640,260,50,50))
        self.addButton.setIconSize(QSize(30,30))
        self.addButton.setStyleSheet(u"border: none; border-radius: 25px; background-color: rgb(109, 141, 223); color: rgb(255, 255, 255);")
    

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
            iconTrashButton.addFile(u"assets/trashLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            trashButton.setIcon(iconTrashButton)
            trashButton.setIconSize(QSize(24, 24))

            self.tableWidget.setCellWidget(row,4,trashButton)
            row += 1
        
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row, 60)
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        
        



    @Slot(int)
    def loadData(self,IDToShow):
        print("IN DAFTAR PEMINJAMAN",IDToShow)
        conn = sqlite3.connect('datarpl.db')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM data_peminjaman_buku WHERE anggota_id = ?',(IDToShow,))
        rows = cursor.fetchall()

        daftar_peminjaman = []
        for row in rows:
            cursor.execute('SELECT judul FROM buku WHERE buku_id = ?',(row[1],))
            title = cursor.fetchall()
            peminjaman = Peminjaman(*row)
            peminjaman.addTitle(title)
            daftar_peminjaman.append(peminjaman)
        
        self.updateTable(daftar_peminjaman)
        
        