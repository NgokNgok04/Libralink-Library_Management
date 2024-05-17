from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class ModalSuccess(QWidget):
    def __init__(self,message,parent=None):
        super().__init__(parent)
        self.setupUi(message)
    
    def setupUi(self,message):
        self.setStyleSheet(u"border: none;")
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        self.layoutModalError = QWidget(self)
        x = (screenSize.width() - 600) // 2
        self.layoutModalError.setStyleSheet(u"background-color: #90EE90; border-radius: 10px;")
        self.layoutModalError.setGeometry(QRect(0,0,600,80))
        self.move(x,50)
        
        self.warningLogo = QPushButton(self)
        self.warningLogo.setGeometry(QRect(0,0,80,80))
        self.warningLogo.setStyleSheet(u"background-color: transparent;")

        icon = QIcon()
        icon.addFile("../../assets/icons/success.png")
        self.warningLogo.setIcon(icon)
        self.warningLogo.setIconSize(QSize(50,50))

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 160))  # Semi-transparent black
        shadow.setOffset(10, 10)  # Offset for X and Y

        self.warningLogo.setGraphicsEffect(shadow)
        
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(True)
        
        self.messageLabel = QLabel(self.layoutModalError)
        self.messageLabel.setText(message)
        self.messageLabel.setFont(font)
        self.messageLabel.setGeometry(QRect(80,0,530,80))
        self.messageLabel.setStyleSheet(u"background-color: transparent; color: white; border: none;")

        timer = QTimer(self)
        timer.timeout.connect(self.timeExpired)
        timer.setSingleShot(False)
        timer.start(2000)
        
    
    def timeExpired(self):
        # print("masuk")
        self.layoutModalError.hide()
        self.warningLogo.hide()

    def setBackgroundColor(self, color):
        self.setStyleSheet(f"background-color: {color}; border-radius: 10px;")