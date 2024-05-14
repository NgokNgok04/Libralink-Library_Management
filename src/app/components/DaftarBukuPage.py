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
    # showDaftarPeminjaman = Signal(bool)
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
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)

        idHeader = QTableWidgetItem()
        judulHeader = QTableWidgetItem()
        isbnHeader = QTableWidgetItem()
        pathHeader = QTableWidgetItem()
        actionHeader = QTableWidgetItem()
        idHeader.setText("ID")
        judulHeader.setText("Judul")
        isbnHeader.setText("ISBN")
        pathHeader.setText("Cover Buku")

        self.tableWidget.setHorizontalHeaderItem(0, idHeader)
        self.tableWidget.setHorizontalHeaderItem(1, judulHeader)
        self.tableWidget.setHorizontalHeaderItem(2, isbnHeader)
        self.tableWidget.setHorizontalHeaderItem(3, pathHeader)
        self.tableWidget.setHorizontalHeaderItem(4, actionHeader)

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

        availableWidth = screenSize.width() - 370
        self.tableWidget.setColumnWidth(0,availableWidth*0.008)
        self.tableWidget.setColumnWidth(1,availableWidth*0.224)
        self.tableWidget.setColumnWidth(2,availableWidth*0.224)
        self.tableWidget.setColumnWidth(3,availableWidth*0.224)
        self.tableWidget.setColumnWidth(4,availableWidth*0.224)
        self.loaddata()

        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row,200)
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

        row = 0
        count = 1
        self.tableWidget.setRowCount(len(daftar_buku))

        for row, buku in enumerate(daftar_buku):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(buku.buku_id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(buku.judul))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(buku.isbn))
            # self.tableWidget.setItem(row, 3, QTableWidgetItem(buku.path))

            pixmap = QPixmap(buku.path)

            scaled_pixmap = pixmap.scaledToWidth(150)

            cover_label = QLabel()
            cover_label.setPixmap(scaled_pixmap) 
            cover_label.setAlignment(Qt.AlignCenter)

            cover_label.setStyleSheet("border-radius: 10px;")

            self.tableWidget.setCellWidget(row, 3, cover_label)

            self.tableWidget.setRowHeight(row, 200)  # Set row height

            widgetAction = QWidget()
            widgetAction.setGeometry(QRect(120,480,134,36))
            HLayoutButton = QHBoxLayout(widgetAction)
            HLayoutButton.setContentsMargins(10,5,0,5)
            PeminjamanButton = QWidget(widgetAction)
            PeminjamanButton.setStyleSheet(u"background-color: rgba(227, 233, 255, 191); border-radius: 12px;")
            HLayoutIsiButton = QHBoxLayout(PeminjamanButton)
            peminjamanLogo = QPushButton(PeminjamanButton)
            peminjamanLogo.clicked.connect(lambda: self.showDaftarPeminjaman.emit(True))
            peminjamanLogo.setStyleSheet(u"background-color: none; border-radius: 0px; border: none;")
            iconPeminjamanLogo = QIcon()
            iconPeminjamanLogo.addFile(u"assets/daftarPeminjamanLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            peminjamanLogo.setIcon(iconPeminjamanLogo)
            HLayoutIsiButton.addWidget(peminjamanLogo)
            dropdownLogo = QPushButton(PeminjamanButton)
            dropdownLogo.clicked.connect(lambda: self.showDaftarPeminjaman.emit(True))
            dropdownLogo.setStyleSheet(u"background-color: none; border: none; border-radius: 10px;")
            iconDropDownLogo = QIcon()
            iconDropDownLogo.addFile(u"assets/dropdownLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            dropdownLogo.setIcon(iconDropDownLogo)
            HLayoutIsiButton.addWidget(dropdownLogo)
            HLayoutButton.addWidget(PeminjamanButton)

            pencilButton = QPushButton(widgetAction)
            pencilButton.setStyleSheet(u"border: none; background-color: none; ")
            iconPencilLogo = QIcon()
            iconPencilLogo.addFile(u"assets/editLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            pencilButton.setIcon(iconPencilLogo)
            pencilButton.setIconSize(QSize(24, 24))
            HLayoutButton.addWidget(pencilButton)

            trashButton = QPushButton(widgetAction)
            trashButton.setCheckable(True)
            trashButton.clicked.connect(lambda: self.showConfirmDelete.emit(True))
            trashButton.clicked.connect(self.handleTrashButtonClicked)
            trashButton.setStyleSheet(u"border: none; background-color: none; ")
            iconTrashButton = QIcon()
            iconTrashButton.addFile(u"assets/trashLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            trashButton.setIcon(iconTrashButton)
            trashButton.setIconSize(QSize(24, 24))
            HLayoutButton.addWidget(trashButton)

            self.tableWidget.setCellWidget(row,4,widgetAction)
            row +=1
            count += 1
        cursor.close()
        conn.close()

    def filterTable(self):
        search_query = self.searchBar.inputSearch.text()
        original_heights = [] 
        original_alignments = [] 

        if not search_query:
            self.loaddata()
            return

        conn = sqlite3.connect('datarpl.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM buku WHERE judul LIKE ?", ('%' + search_query + '%',))
        rows = cursor.fetchall()

        daftar_buku = []
        for row in rows:
            buku = Buku(*row)
            daftar_buku.append(buku)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        for buku in daftar_buku:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(buku.buku_id)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(buku.judul))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(buku.isbn))

            pixmap = QPixmap(buku.path)
            scaled_pixmap = pixmap.scaledToWidth(150)

            cover_label = QLabel()
            cover_label.setPixmap(scaled_pixmap)
            cover_label.setAlignment(Qt.AlignCenter)
            cover_label.setStyleSheet("border-radius: 10px;")

            self.tableWidget.setCellWidget(row_position, 3, cover_label)

            self.tableWidget.setRowHeight(row_position, 200) 

            widgetAction = QWidget()
            widgetAction.setGeometry(QRect(120,480,134,36))
            HLayoutButton = QHBoxLayout(widgetAction)
            HLayoutButton.setContentsMargins(10,5,0,5)
            PeminjamanButton = QWidget(widgetAction)
            PeminjamanButton.setStyleSheet(u"background-color: rgba(227, 233, 255, 191); border-radius: 12px;")
            HLayoutIsiButton = QHBoxLayout(PeminjamanButton)
            peminjamanLogo = QPushButton(PeminjamanButton)
            peminjamanLogo.clicked.connect(lambda: self.showDaftarPeminjaman.emit(True))
            peminjamanLogo.setStyleSheet(u"background-color: none; border-radius: 0px; border: none;")
            iconPeminjamanLogo = QIcon()
            iconPeminjamanLogo.addFile(u"assets/daftarPeminjamanLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            peminjamanLogo.setIcon(iconPeminjamanLogo)
            HLayoutIsiButton.addWidget(peminjamanLogo)
            dropdownLogo = QPushButton(PeminjamanButton)
            dropdownLogo.clicked.connect(lambda: self.showDaftarPeminjaman.emit(True))
            dropdownLogo.setStyleSheet(u"background-color: none; border: none; border-radius: 10px;")
            iconDropDownLogo = QIcon()
            iconDropDownLogo.addFile(u"assets/dropdownLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            dropdownLogo.setIcon(iconDropDownLogo)
            HLayoutIsiButton.addWidget(dropdownLogo)
            HLayoutButton.addWidget(PeminjamanButton)

            pencilButton = QPushButton(widgetAction)
            pencilButton.setStyleSheet(u"border: none; background-color: none; ")
            iconPencilLogo = QIcon()
            iconPencilLogo.addFile(u"assets/editLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            pencilButton.setIcon(iconPencilLogo)
            pencilButton.setIconSize(QSize(24, 24))
            HLayoutButton.addWidget(pencilButton)

            trashButton = QPushButton(widgetAction)
            trashButton.setStyleSheet(u"border: none; background-color: none; ")
            iconTrashButton = QIcon()
            iconTrashButton.addFile(u"assets/trashLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            trashButton.setIcon(iconTrashButton)
            trashButton.setIconSize(QSize(24, 24))
            HLayoutButton.addWidget(trashButton)

            self.tableWidget.setCellWidget(row_position, 4, widgetAction)

            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHeight(row,200)
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    if item:
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        
    # def handleItemClicked(self, item):
    #     # Get the row index of the clicked item
    #     # row = item.row()
    #     row = self.tableWidget.row(item)

    #     # Retrieve the ID from the first column of the clicked row
    #     # Assuming the ID is stored in the first column
    #     id_item = self.tableWidget.item(row, 0)
    #     if id_item:
    #         self.selectedRowId = int(id_item.text())
    
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
