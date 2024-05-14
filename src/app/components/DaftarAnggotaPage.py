# DaftarAnggotaPage.py
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from components.SearchBar import SearchBar
import resource
import sqlite3
# from components.DeleteConfirmationForm import DeleteConfirmationForm

class Anggota:
    def __init__(self, anggota_id, nama, email, telephone, status_anggota):
        self.anggota_id = anggota_id
        self.nama = nama
        self.email = email
        self.telephone = telephone
        self.status_anggota = status_anggota

class DaftarAnggotaPage(QWidget):
    showDaftarPeminjaman = Signal(bool)
    showConfirmDelete = Signal(bool)
    selectedRowId = None

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        self.layoutDaftarAnggota = QWidget(self)
        self.layoutDaftarAnggota.setGeometry(QRect(0, 0, screenSize.width() - 370, screenSize.height() - 250))
        
        self.searchBar = SearchBar(self.layoutDaftarAnggota)
        self.searchBar.inputSearch.setPlaceholderText("Cari Anggota")
        self.searchBar.inputSearch.textChanged.connect(self.filterData)

        self.tableWidget = QTableWidget(self.layoutDaftarAnggota)
        if self.tableWidget.columnCount() < 6:
            self.tableWidget.setColumnCount(6)

        idHeader = QTableWidgetItem()
        namaHeader = QTableWidgetItem()
        emailHeader = QTableWidgetItem()
        teleponHeader = QTableWidgetItem()
        statusHeader = QTableWidgetItem()
        actionHeader = QTableWidgetItem()
        idHeader.setText("ID")
        namaHeader.setText("Nama")
        emailHeader.setText("Alamat Email")
        teleponHeader.setText("No Telepon")
        statusHeader.setText("Status")

        self.tableWidget.setHorizontalHeaderItem(0, idHeader)
        self.tableWidget.setHorizontalHeaderItem(1, namaHeader)
        self.tableWidget.setHorizontalHeaderItem(2, emailHeader)
        self.tableWidget.setHorizontalHeaderItem(3, teleponHeader)
        self.tableWidget.setHorizontalHeaderItem(4, statusHeader)
        self.tableWidget.setHorizontalHeaderItem(5, actionHeader)

        self.tableWidget.setGeometry(QRect(0, 60, screenSize.width() - 370, screenSize.height() - 250))
        self.tableWidget.setMinimumSize(QSize(1021, 192))
        self.tableWidget.setMaximumSize(QSize(screenSize.width(), screenSize.height()))
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"    font-weight: bold;\n"
"    color: rgb(130, 130, 130);\n"
"    border: none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget{\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border: none;\n"
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
        self.tableWidget.setColumnWidth(0, availableWidth * 0.008)
        self.tableWidget.setColumnWidth(1, availableWidth * 0.169)
        self.tableWidget.setColumnWidth(2, availableWidth * 0.254)
        self.tableWidget.setColumnWidth(3, availableWidth * 0.186)
        self.tableWidget.setColumnWidth(4, availableWidth * 0.144)
        self.tableWidget.setColumnWidth(5, availableWidth * 0.144)
        self.loaddata()

        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row, 45)
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # self.tableWidget.itemClicked.connect(self.handleItemClicked)
    def loaddata(self):
        conn = sqlite3.connect('datarpl.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM anggota')
        rows = cursor.fetchall()
        
        daftar_anggota = []
        for row in rows:
            anggota = Anggota(*row)
            daftar_anggota.append(anggota)

        self.updateTable(daftar_anggota)

        cursor.close()
        conn.close()

    def updateTable(self, data):
        self.tableWidget.setRowCount(len(data))

        for row, anggota in enumerate(data):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(anggota.anggota_id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(anggota.nama))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(anggota.email))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(anggota.telephone))
            if str(anggota.status_anggota) == "1":
                nonActive = QPushButton("Nonaktif")
                nonActive.setStyleSheet("color: rgb(235, 87, 87); background-color: rgba(248, 0, 0, 51); border-radius: 20px;")
                nonActive.setFixedHeight(144)
                nonActive.setFixedHeight(40)
                font = QFont()
                font.setPointSize(10)
                font.setBold(True)
                nonActive.setFont(font)
                self.tableWidget.setCellWidget(row, 4, nonActive)
            else:
                active = QPushButton("Aktif")
                active.setStyleSheet("color: rgb(39, 174, 96); background-color: rgba(3, 171, 0, 51); border-radius: 20px;")
                active.setFixedHeight(144)
                active.setFixedHeight(40)
                font = QFont()
                font.setPointSize(10)
                font.setBold(True)
                active.setFont(font)
                self.tableWidget.setCellWidget(row, 4, active)

            self.tableWidget.setRowHeight(row, 45)

            widgetAction = QWidget()
            widgetAction.setGeometry(QRect(120, 480, 134, 36))
            HLayoutButton = QHBoxLayout(widgetAction)
            HLayoutButton.setContentsMargins(10, 5, 0, 5)
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
            # trashButton.clicked.connect(lambda: self.handleItemClicked(QTableWidgetItem()))
            trashButton.clicked.connect(self.handleTrashButtonClicked)
            trashButton.setStyleSheet(u"border: none; background-color: none; ")
            iconTrashButton = QIcon()
            iconTrashButton.addFile(u"assets/trashLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            trashButton.setIcon(iconTrashButton)
            trashButton.setIconSize(QSize(24, 24))
            HLayoutButton.addWidget(trashButton)

            self.tableWidget.setCellWidget(row, 5, widgetAction)
            row += 1

            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHeight(row, 45)
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    if item:
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def filterData(self, search_query):
        conn = sqlite3.connect('datarpl.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM anggota WHERE nama LIKE ?', ('%' + search_query + '%',))
        rows = cursor.fetchall()
        
        daftar_anggota = []
        for row in rows:
            anggota = Anggota(*row)
            daftar_anggota.append(anggota)

        self.updateTable(daftar_anggota)

        cursor.close()
        conn.close()
    
    # def handleItemClicked(self, item):
    #     # Get the row index of the clicked item
    #     # row = item.row()
    #     row = self.tableWidget.row(item)

    #     # Retrieve the ID from the first column of the clicked row
    #     # Assuming the ID is stored in the first column
    #     id_item = self.tableWidget.item(row, 0)
    #     if id_item:
    #         self.selectedRowId = int(id_item.text())

    def handleItemClicked(self, item):
        if item is not None:  # Check if item is valid
            row = self.tableWidget.row(item)
            if row >= 0:  # Check if row index is valid
                id_item = self.tableWidget.item(row, 0)
                if id_item is not None:  # Check if ID item is valid
                    self.selectedRowId = int(id_item.text())
                    # Print selected row ID and data
                    print("Selected Row ID:", self.selectedRowId)
                    # row_data = [self.tableWidget.item(row, col).text() for col in range(self.tableWidget.columnCount())]
                    # print("Selected Row Data:", row_data)
                else:
                    print("ID item is None")
            else:
                print("Invalid row index:", row)
        else:
            print("Clicked item is None")
    
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
    def confirmDeletion(self, confirmDeleteSignal):
        if confirmDeleteSignal and self.selectedRowId is not None:
            print("bye)")
            # Connect to your database
            conn = sqlite3.connect('datarpl.db')
            cursor = conn.cursor()

            # Execute the DELETE query using the selectedRowId
            cursor.execute('DELETE FROM anggota WHERE anggota_id = ?', (self.selectedRowId,))
            conn.commit()

            # Close the connection
            cursor.close()
            conn.close()

            # Optional: Refresh the table or UI to reflect the changes
            self.loaddata()
        print("awdawdawdasdawd)")
        
    