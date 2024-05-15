from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from components.SearchBar import SearchBar
import resource
import sqlite3

class Buku:
    def __init__(self, buku_id, judul, isbn, path):
        self.buku_id = buku_id
        self.judul = judul
        self.isbn = isbn
        self.path = path

class DaftarBukuPage(QWidget):
    showConfirmDelete = Signal(bool)
    selectedRowId = None

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        self.layoutDaftarBuku = QWidget(self)
        self.layoutDaftarBuku.setGeometry(QRect(0,0,screenSize.width() - 370,screenSize.height() - 250))
        # self.setGeometry(QRect(0,0,10,10))
        self.searchBar = SearchBar(self.layoutDaftarBuku)
        self.searchBar.inputSearch.setPlaceholderText("Cari Buku")
        self.searchBar.inputSearch.textChanged.connect(self.filterTable)

        self.tableWidget = QTableWidget(self.layoutDaftarBuku)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)

        idHeader = QTableWidgetItem()
        coverHeader = QTableWidgetItem()
        judulHeader = QTableWidgetItem()
        isbnHeader = QTableWidgetItem()
        statusHeader = QTableWidgetItem()
        actionHeader = QTableWidgetItem()

        idHeader.setText("ID")
        coverHeader.setText("Cover Buku")
        judulHeader.setText("Judul")
        isbnHeader.setText("ISBN")
        statusHeader.setText("Status")

        self.tableWidget.setHorizontalHeaderItem(0, idHeader)
        self.tableWidget.setHorizontalHeaderItem(1, coverHeader)
        self.tableWidget.setHorizontalHeaderItem(2, judulHeader)
        self.tableWidget.setHorizontalHeaderItem(3, isbnHeader)
        self.tableWidget.setHorizontalHeaderItem(4, statusHeader)
        self.tableWidget.setHorizontalHeaderItem(5, actionHeader)

        self.tableWidget.setGeometry(QRect(0, 60, screenSize.width() - 370, screenSize.height() - 250))
        self.tableWidget.setMinimumSize(QSize(1021, 192))
        self.tableWidget.setMaximumSize(QSize(screenSize.width(),screenSize.height()))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.tableWidget.setFont(font)
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

        availableWidth = self.tableWidget.width() - 340
        print(availableWidth)
        self.tableWidget.setColumnWidth(0,10) #Fixed
        self.tableWidget.setColumnWidth(1,availableWidth // 3)
        self.tableWidget.setColumnWidth(2,availableWidth // 3)
        self.tableWidget.setColumnWidth(3,150) #Fixed
        self.tableWidget.setColumnWidth(4,180) #Fixed
        self.tableWidget.setColumnWidth(5,availableWidth - 2*(availableWidth //3)) 
        self.loaddata()
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row,164)
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def loaddata(self):
        conn = sqlite3.connect('datarpl.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM buku')
        rows = cursor.fetchall()
        
        daftar_buku = []
        for row in rows:
            buku = Buku(*row)
            daftar_buku.append(buku)
        
        self.updateTable(daftar_buku)

        cursor.close()
        conn.close()
    
    def updateTable(self,data):
        self.tableWidget.setRowCount(len(data))

        for row, buku in enumerate(data):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(buku.buku_id)))

            self.coverButton = QPushButton()
            iconCover = QIcon()
            iconCover.addFile(buku.path)
            self.coverButton.setIcon(iconCover)
            self.coverButton.setIconSize(QSize(200,200))
            self.coverButton.setStyleSheet(u"border: none;")
            self.tableWidget.setCellWidget(row,1, self.coverButton)

            self.tableWidget.setItem(row, 2, QTableWidgetItem(buku.judul))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(buku.isbn))


            # nonActive = QPushButton("Nonaktif")
            # nonActive.setStyleSheet("color: rgb(235, 87, 87); background-color: rgba(248, 0, 0, 51); border-radius: 20px;")
            # nonActive.setFixedHeight(144)
            # nonActive.setFixedHeight(40)
            # font = QFont()
            # font.setPointSize(10)
            # font.setBold(True)
            # nonActive.setFont(font)
            # self.tableWidget.setCellWidget(row, 4, nonActive)

            self.widgetStatus = QWidget()
            self.widgetIsiStatus = QWidget(self.widgetStatus)
            self.statusButton = QPushButton(self.widgetIsiStatus)
            self.statusButton.setText("Tersedia")
            self.statusButton.setStyleSheet("color: rgb(39, 174, 96); background-color: rgba(3, 171, 0, 51); border-radius: 20px;")
            # 164 - 40 / 2
            self.statusButton.setGeometry(QRect(15,62,150,40))
            font = QFont()
            font.setPointSize(11)
            font.setBold(True)
            self.statusButton.setFont(font)
            self.tableWidget.setCellWidget(row, 4, self.widgetStatus)

            self.widgetAction = QWidget()
            self.widgetIsiAction = QWidget(self.widgetAction)

            self.coverPencilLogo = QPushButton(self.widgetIsiAction)
            self.coverPencilLogo.setGeometry(QRect(5,62,40,40))
            self.coverPencilLogo.setStyleSheet(u"border: none;")
            self.iconCoverPencilLogo = QIcon()
            self.iconCoverPencilLogo.addFile(u"assets/editLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            self.coverPencilLogo.setIcon(self.iconCoverPencilLogo)
            self.coverPencilLogo.setIconSize(QSize(30,30))

            self.coverTrashLogo = QPushButton(self.widgetIsiAction)
            self.coverTrashLogo.setGeometry(QRect(50,62,40,40))
            self.coverTrashLogo.setStyleSheet(u"border: none;")
            self.iconCoverTrashLogo = QIcon()
            self.iconCoverTrashLogo.addFile(u"assets/trashLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            self.coverTrashLogo.setIcon(self.iconCoverTrashLogo)
            self.coverTrashLogo.setIconSize(QSize(30,30))
            self.coverTrashLogo.clicked.connect(lambda: self.showConfirmDelete.emit(True))
            self.coverTrashLogo.clicked.connect(self.handleTrashButtonClicked)

            self.tableWidget.setCellWidget(row,5,self.widgetAction)
            row+=1
    
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row, 164)
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)



    def filterTable(self,search_query):
        conn = sqlite3.connect('datarpl.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM buku WHERE judul LIKE ?", ('%' + search_query + '%',))
        rows = cursor.fetchall()

        daftar_buku = []
        for row in rows:
            buku = Buku(*row)
            daftar_buku.append(buku)

        self.updateTable(daftar_buku)

        cursor.close()
        conn.close()
                        
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
                    print("Selected Row ID:", self.selectedRowId)
                else:
                    print("ID item is None")
            else:
                print("Invalid index")
        else:
            print("Sender button is None")
    
    @Slot(bool)
    def confirmDeletion(self, confirmed):
        if confirmed and self.selectedRowId is not None:
            # Connect to your database
            conn = sqlite3.connect('datarpl.db')
            cursor = conn.cursor()

            # Execute the DELETE query using the selectedRowId
            cursor.execute('DELETE FROM buku WHERE buku_id = ?', (self.selectedRowId,))
            conn.commit()

            # Close the connection
            cursor.close()
            conn.close()

            # Optional: Refresh the table or UI to reflect the changes
            self.loaddata()
