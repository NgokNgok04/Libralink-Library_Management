from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from components.Header import Header
from components.Sidebar import Sidebar
from components.AddButton import AddButton
# from components.TemplateDaftarAnggota import TemplateDaftarAnggota

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("LibraLink Management")
        screenSize = QGuiApplication.primaryScreen().availableGeometry()

        self.resize(screenSize.width(), screenSize.height())
        self.setMinimumSize(QSize(screenSize.width(), screenSize.height()))
        self.setMaximumSize(QSize(screenSize.width(), screenSize.height()))
        self.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.headerWidget = Header(self.centralwidget)
        self.sidebarWidget = Sidebar(self.centralwidget)
        self.addButton = AddButton(self.centralwidget)
        self.addButton.setGeometry(QRect(screenSize.width() - 80, screenSize.height() - 105, 70, 70))
        self.sidebarWidget.showWidget.connect(self.headerWidget.changeStackedWidgetIndex)
        self.headerWidget.showAddButton.connect(self.addButton.isShowAddButton)
        
        self.headerWidget.setContentsMargins(0, 0, 0, 0)
