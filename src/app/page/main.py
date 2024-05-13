from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget
from PySide6.QtGui import QGuiApplication, QFont,QIcon
from PySide6.QtCore import Qt, QRect,QSize
import sys
from DaftarAnggota import Ui_MainWindow
from Header import HeaderWidget
import sqlite3

class Anggota:
    def __init__(self,anggota_id,nama, email, telephone, status_anggota):
        self.anggota_id = anggota_id
        self.nama = nama
        self.email = email
        self.telephone = telephone
        self.status_anggota = status_anggota

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Window")
        self.tableWidget.setColumnWidth(0,1)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,300)
        self.tableWidget.setColumnWidth(3,220)
        self.tableWidget.setColumnWidth(4,170)
        self.tableWidget.setColumnWidth(5,170)
        self.showMaximized()
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        print(f"Full screen dimensions: {screen_geometry.width()}x{screen_geometry.height()}")
        # self.tableWidget.setRowWidth(0,100)
        self.loaddata()
        # Set tableWidget items and center-align them
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(row,45)
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    
    def loaddata(self):
        conn = sqlite3.connect('datarpl.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM anggota')
        rows = cursor.fetchall()
        
        daftar_anggota = []
        for row in rows:
            anggota = Anggota(*row)
            daftar_anggota.append(anggota)

        row = 0
        count = 1
        self.tableWidget.setRowCount(len(daftar_anggota))

        for row, anggota in enumerate(daftar_anggota):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(anggota.anggota_id)))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(anggota.nama))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(anggota.email))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(anggota.telephone))
            if (str(anggota.status_anggota) == "1"):
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
                self.tableWidget.setCellWidget(row,4,active)


            widgetAction = QWidget()
            widgetAction.setGeometry(QRect(120,480,134,36))
            HLayoutButton = QHBoxLayout(widgetAction)
            HLayoutButton.setContentsMargins(10,5,0,5)
            PeminjamanButton = QWidget(widgetAction)
            PeminjamanButton.setStyleSheet(u"background-color: rgba(227, 233, 255, 191); border-radius: 12px;")
            HLayoutIsiButton = QHBoxLayout(PeminjamanButton)
            peminjamanLogo = QPushButton(PeminjamanButton)
            peminjamanLogo.setStyleSheet(u"background-color: none; border-radius: 0px; border: none;")
            iconPeminjamanLogo = QIcon()
            iconPeminjamanLogo.addFile(u":/assets/daftarPeminjamanLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            peminjamanLogo.setIcon(iconPeminjamanLogo)
            HLayoutIsiButton.addWidget(peminjamanLogo)
            dropdownLogo = QPushButton(PeminjamanButton)
            dropdownLogo.setStyleSheet(u"background-color: none; border: none; border-radius: 10px;")
            iconDropDownLogo = QIcon()
            iconDropDownLogo.addFile(u":/assets/dropdownLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            dropdownLogo.setIcon(iconDropDownLogo)
            HLayoutIsiButton.addWidget(dropdownLogo)
            HLayoutButton.addWidget(PeminjamanButton)

            pencilButton = QPushButton(widgetAction)
            pencilButton.setStyleSheet(u"border: none; background-color: none; ")
            iconPencilLogo = QIcon()
            iconPencilLogo.addFile(u":/assets/editLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            pencilButton.setIcon(iconPencilLogo)
            pencilButton.setIconSize(QSize(24, 24))
            HLayoutButton.addWidget(pencilButton)

            trashButton = QPushButton(widgetAction)
            trashButton.setStyleSheet(u"border: none; background-color: none; ")
            iconTrashButton = QIcon()
            iconTrashButton.addFile(u":/assets/trashLogo.png", QSize(), QIcon.Normal, QIcon.Off)
            trashButton.setIcon(iconTrashButton)
            trashButton.setIconSize(QSize(24, 24))
            HLayoutButton.addWidget(trashButton)

            self.tableWidget.setCellWidget(row,5,widgetAction)
            row +=1
            count += 1
        cursor.close()
        conn.close()

app = QApplication(sys.argv)

window = MySideBar()

window.show()

app.exec()