from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QWidget)
from DaftarAnggota import Ui_MainWindow
import resources

class HeaderWidget(QMainWindow, Ui_MainWindow):
    def setupUi(self,centralWidget):
        self.headerWidget = QWidget(centralWidget)
        self.headerWidget.setGeometry(QRect(0, 0, 1541, 178))
        self.headerWidget.setStyleSheet(u"background-color: rgb(109, 141, 223);")
        
        self.layoutWidget = QWidget(self.headerWidget)
        self.layoutWidget.setGeometry(QRect(30, 20, 338, 72))
        
        self.HLayoutLogo = QHBoxLayout(self.layoutWidget)
        self.HLayoutLogo.setContentsMargins(0, 0, 0, 0)
        self.logoLibraLink = QLabel(self.layoutWidget)

        self.logoLibraLink.setMinimumSize(QSize(70, 70))
        self.logoLibraLink.setMaximumSize(QSize(70, 70))
        self.logoLibraLink.setPixmap(QPixmap(u":/assets/libraLinkLogo.png"))
        self.HLayoutLogo.addWidget(self.logoLibraLink)

        self.logoTitle = QLabel(self.layoutWidget)
        fontLogoTitle = QFont()
        fontLogoTitle.setPointSize(12)
        fontLogoTitle.setBold(True)
        self.logoTitle.setFont(fontLogoTitle)
        self.logoTitle.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.HLayoutLogo.addWidget(self.logoTitle)

        self.stackedWidgetDirectory = QStackedWidget(self.headerWidget)
        self.stackedWidgetDirectory.setGeometry(QRect(360, 120, 481, 61))
        
        self.HomeDirectory = QWidget()
        self.HomeLabel = QLabel(self.HomeDirectory)
        self.HomeLabel.setGeometry(QRect(10, 10, 101, 41))

        fontDirectory = QFont()
        fontDirectory.setPointSize(17)
        fontDirectory.setBold(True)
        self.HomeLabel.setFont(fontDirectory)
        self.HomeLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.HomeDirectory)

        self.DaftarBukuDirectory = QWidget()
        self.DaftarBukuLabel = QLabel(self.DaftarBukuDirectory)
        self.DaftarBukuLabel.setGeometry(QRect(10, 10, 381, 41))
        self.DaftarBukuLabel.setFont(fontDirectory)
        self.DaftarBukuLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.DaftarBukuDirectory)

        self.DaftarAnggotaDirectory = QWidget()
        self.DaftarAnggotaLabel = QLabel(self.DaftarAnggotaDirectory)
        self.DaftarAnggotaLabel.setGeometry(QRect(10, 10, 431, 41))
        self.DaftarAnggotaLabel.setFont(fontDirectory)
        self.DaftarAnggotaLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidgetDirectory.addWidget(self.DaftarAnggotaDirectory)
    
    def retranslateUi(self,centralWidget):
        self.logoLibraLink.setText("")
        self.logoTitle.setText(QCoreApplication.translate("MainWindow", u"Libralink Management", None))
        self.HomeLabel.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.DaftarBukuLabel.setText(QCoreApplication.translate("MainWindow", u"Daftar Buku Perpustakaan", None))
        self.DaftarAnggotaLabel.setText(QCoreApplication.translate("MainWindow", u"Daftar Anggota Perpustakaan", None))