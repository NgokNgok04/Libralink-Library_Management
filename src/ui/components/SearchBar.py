from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class SearchBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        self.layoutSearchBar = QWidget(self)
        self.layoutSearchBar.setGeometry(QRect(screenSize.width() - 900,0,541,55))
        self.inputSearch = QLineEdit(self.layoutSearchBar)
        self.inputSearch.setGeometry(QRect(0, 10, 481, 41))
        self.inputSearch.setStyleSheet(u"QLineEdit {\n"
"	color: black;\n"
"	padding-left: 10px;\n"
"	padding-top: 10px;\n"
"	padding-bottom: 10px;\n"
"	border-top: 1px solid rgb(100, 119, 219);\n"
"	border-left: 1px solid rgb(100, 119, 219);\n"
"	border-bottom: 1px solid rgb(100, 119, 219);\n"
"	border-top-left-radius: 20px;\n"
"	border-bottom-left-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"	\n"
"	color: rgb(189, 189, 189);\n"
"	padding-left: 10px;\n"
"}")
        self.buttonSearch = QPushButton(self.layoutSearchBar)
        self.buttonSearch.setObjectName(u"buttonSearch")
        self.buttonSearch.setGeometry(QRect(480, 10, 41, 41))
        self.buttonSearch.setStyleSheet(u"QPushButton{\n"
"	border-top: 1px solid rgb(100, 119, 219);\n"
"	border-right: 1px solid rgb(100, 119, 219);\n"
"	border-bottom: 1px solid rgb(100, 119, 219); \n"
"	border-top-right-radius: 17px;\n"
"	border-bottom-right-radius: 17px;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../assets/icons/searchFaceLeft.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonSearch.setIcon(icon)
        self.buttonSearch.setIconSize(QSize(18, 18))