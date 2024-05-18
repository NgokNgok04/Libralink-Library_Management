from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
icons_folder = os.path.join(os.path.dirname(__file__), '../../../assets/icons')
os.makedirs(icons_folder, exist_ok=True)
class AddButton(QPushButton):
    def __init__(self, parent=None, clicked=None):
        super().__init__(parent)
        self.clicked.connect(clicked)
        self.setupUi()
    
    def setupUi(self):
        self.setStyleSheet(u"border: none; border-radius: 35px; background-color: rgb(109, 141, 223); color: rgb(255, 255, 255);")
        icon5 = QIcon()

        iconAddLogo_path = os.path.join(icons_folder, 'addButton.png')
        icon5.addFile(iconAddLogo_path, QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon5)
        self.setIconSize(QSize(34, 34))
        self.setCheckable(True)
        self.setAutoExclusive(True)

        self.setDefault(False)
    
    @Slot(bool)
    def isShowAddButton(self, isShow):
        if (isShow):
            self.show()
        else:
            self.hide()