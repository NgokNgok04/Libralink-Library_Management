from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from components.AddButton import AddButton
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
        self.cancelButton.setStyleSheet(u"background-color: none; border: none;")
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

        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,230)
        self.tableWidget.setColumnWidth(2,120)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,130)

        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setGeometry(QRect(10, 80, 681, 175))
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
"}    ")




        self.addButton = AddButton(self.layoutDaftarPeminjaman)
        self.addButton.setGeometry(QRect(640,260,50,50))
        self.addButton.setIconSize(QSize(30,30))
        self.addButton.setStyleSheet(u"border: none; border-radius: 25px; background-color: rgb(109, 141, 223); color: rgb(255, 255, 255);")

