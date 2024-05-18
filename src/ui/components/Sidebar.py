from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import os
icons_folder = os.path.join(os.path.dirname(__file__), '../../../assets/icons')
os.makedirs(icons_folder, exist_ok=True)

class Sidebar(QWidget):
    showWidget = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        # Get screen size
        screenSize = QGuiApplication.primaryScreen().availableGeometry()

        # Sidebar layout
        self.layoutSidebar = QWidget(self)
        self.layoutSidebar.setGeometry(QRect(20, 120, 321, screenSize.height() - 180))
        self.layoutSidebar.setStyleSheet("border-radius: 10px; border: 2px solid rgb(100, 119, 219);")

        # Font setup
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)

        # Profile name label
        self.profileName = QLabel(self.layoutSidebar)
        self.profileName.setGeometry(QRect(71, 128, 178, 24))
        self.profileName.setFont(font)
        self.profileName.setStyleSheet("color: rgb(0, 0, 0); border: none;")
        self.profileName.setAlignment(Qt.AlignCenter)
        self.profileName.setText("Daniel the Great")

        # Administrator button
        self.administrator = QPushButton(self.layoutSidebar)
        self.administrator.setGeometry(QRect(90, 160, 141, 31))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.administrator.setFont(font2)
        self.administrator.setStyleSheet("background-color: rgba(111, 207, 151, 51); color: rgb(111, 207, 151); border-radius: 15px; border: none;")
        self.administrator.setText("Administrator")

        # Profile image button
        self.profileImage = QPushButton(self.layoutSidebar)
        self.profileImage.setGeometry(QRect(106, 22, 103, 99))
        self.profileImage.setStyleSheet("border:none;")
        icon = QIcon()
        iconPP_path = os.path.join(icons_folder, 'profilePlaceHolder.png')
        icon.addFile(iconPP_path, QSize(), QIcon.Normal, QIcon.Off)
        self.profileImage.setIcon(icon)
        self.profileImage.setIconSize(QSize(99, 99))
        self.profileImage.setText("")

        # Home sidebar button
        self.HomeSidebar = QPushButton(self.layoutSidebar)
        self.HomeSidebar.setGeometry(QRect(21, 231, 281, 50))
        self.HomeSidebar.setFont(font)
        self.HomeSidebar.setStyleSheet("""
            QPushButton {
                color: rgb(0, 0, 0);
                text-align: left;
                height: 30px;
                border: none;
                padding-left: 20px;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 20px;
            }
            QPushButton:checked {
                color: rgb(100, 119, 219);
                background-color: rgba(227, 233, 255, 191);
            }
        """)
        icon1 = QIcon()
        iconHome_path = os.path.join(icons_folder, 'homelogo2.png')
        icon1.addFile(iconHome_path, QSize(), QIcon.Normal, QIcon.Off)
        self.HomeSidebar.setIcon(icon1)
        self.HomeSidebar.setIconSize(QSize(40, 40))
        self.HomeSidebar.setCheckable(True)
        self.HomeSidebar.setAutoExclusive(True)
        self.HomeSidebar.setChecked(True)
        self.HomeSidebar.setText("Home")
        self.HomeSidebar.clicked.connect(lambda: self.showWidget.emit(0))

        # Buku sidebar button
        self.BukuSidebar = QPushButton(self.layoutSidebar)
        self.BukuSidebar.setGeometry(QRect(21, 291, 281, 50))
        self.BukuSidebar.setFont(font)
        self.BukuSidebar.setStyleSheet("""
            QPushButton {
                color: rgb(0, 0, 0);
                text-align: left;
                height: 30px;
                border: none;
                padding-left: 20px;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 20px;
            }
            QPushButton:checked {
                color: rgb(100, 119, 219);
                background-color: rgba(227, 233, 255, 191);
            }
        """)
        icon2 = QIcon()
        iconDaftarBuku_path = os.path.join(icons_folder, 'daftarBukuLogo.png')
        icon2.addFile(iconDaftarBuku_path, QSize(), QIcon.Normal, QIcon.Off)
        self.BukuSidebar.setIcon(icon2)
        self.BukuSidebar.setIconSize(QSize(40, 40))
        self.BukuSidebar.setCheckable(True)
        self.BukuSidebar.setAutoExclusive(True)
        self.BukuSidebar.setText("Daftar Buku")
        self.BukuSidebar.clicked.connect(lambda: self.showWidget.emit(1))

        # Anggota sidebar button
        self.AnggotaSidebar = QPushButton(self.layoutSidebar)
        self.AnggotaSidebar.setGeometry(QRect(21, 351, 281, 50))
        self.AnggotaSidebar.setFont(font)
        self.AnggotaSidebar.setStyleSheet("""
            QPushButton {
                color: rgb(0, 0, 0);
                text-align: left;
                height: 30px;
                border: none;
                padding-left: 20px;
                padding-top: 10px;
                padding-bottom: 10px;
                border-radius: 20px;
            }
            QPushButton:checked {
                color: rgb(100, 119, 219);
                background-color: rgba(227, 233, 255, 191);
            }
        """)
        icon3 = QIcon()
        iconDaftarAnggota_path = os.path.join(icons_folder, 'daftarAnggotaLogo.png')
        icon3.addFile(iconDaftarAnggota_path, QSize(), QIcon.Normal, QIcon.Off)
        self.AnggotaSidebar.setIcon(icon3)
        self.AnggotaSidebar.setIconSize(QSize(40, 40))
        self.AnggotaSidebar.setCheckable(True)
        self.AnggotaSidebar.setAutoExclusive(True)
        self.AnggotaSidebar.setText("Daftar Anggota")
        self.AnggotaSidebar.clicked.connect(lambda: self.showWidget.emit(2))

    @Slot(int)
    def changeButton(self, theint):
        if theint == 1:
            self.BukuSidebar.setChecked(True)
        else:
            self.AnggotaSidebar.setChecked(True)

