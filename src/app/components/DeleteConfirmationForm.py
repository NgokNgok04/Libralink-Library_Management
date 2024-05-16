from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class DeleteConfirmationForm(QWidget):
    showConfirmDelete = Signal(bool)
    confirmDeleteSignal = Signal(bool)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    
    def setupUi(self):
        screenSize = QGuiApplication.primaryScreen().geometry()
        self.layoutDaftarPeminjaman = QWidget(self)
        x = (screenSize.width() - 300) // 2
        y = (screenSize.height() - 150) // 2
        self.layoutDaftarPeminjaman.setGeometry(0, 0, 300, 150)
        self.move(x, y)

        self.setStyleSheet(u"border: none;")

        self.layoutDaftarPeminjaman.setStyleSheet(u"background-color: #666666; border: 1px solid rgb(109, 141, 223); border-radius: 14px")
        self.title = QLabel(self)
        self.title.setText("Apakah anda yakin\ningin menghapus  ini?")
        self.title.setStyleSheet(u"background-color: transparent; color:white;")
        self.title.setGeometry(QRect(25, 20, 250, 50))  # Adjusted height to accommodate two lines
        self.title.setAlignment(Qt.AlignCenter)  # Center-align the text

        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.cancelButton = QPushButton(self.layoutDaftarPeminjaman)
        self.cancelButton.setText("Batal")
        self.cancelButton.setFont(font)
        self.cancelButton.setGeometry(QRect(45, 80, 100, 40))
        self.cancelButton.setStyleSheet(u"background-color: #EB5757; color: white; border: none; border-radius: 5px;")
        self.cancelButton.clicked.connect(lambda: self.showConfirmDelete.emit(False))

        self.confirmButton = QPushButton(self.layoutDaftarPeminjaman)
        self.confirmButton.setText("Ya")
        self.confirmButton.setFont(font)
        self.confirmButton.setGeometry(QRect(155, 80, 100, 40))
        self.confirmButton.setStyleSheet(u"background-color: #6FCF97; color: white; border: none; border-radius: 5px;")
        # self.confirmButton.clicked.connect(self.confirmDelete)
        self.confirmButton.clicked.connect(lambda: self.showConfirmDelete.emit(False))
        self.confirmButton.clicked.connect(lambda: self.confirmDeleteSignal.emit(True))

    # def confirmDelete(self):
    #     self.showConfirmDelete.emit(True)

    # def confirmDeleteAction(self):
    #     # Emit the confirmDeleteSignal when "Ya" button is clicked
    #     self.confirmDeleteSignal.emit(True)
