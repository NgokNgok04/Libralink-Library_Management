from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os

class HomePage(QWidget):
    whatsShowing = Signal(int)
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        screenSize = QGuiApplication.primaryScreen().availableGeometry()
        self.setGeometry(QRect(0, 0, screenSize.width() - 370, screenSize.height() - 250))

        # Load and register the custom font
        font_folder = os.path.join(os.path.dirname(__file__), '../../../assets/fonts')
        os.makedirs(font_folder, exist_ok=True)
        font_path = os.path.join(font_folder, 'Heavitas.ttf')

        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        # Welcome label
        welcomeLabel = QLabel("WELCOME", self)
        welcomeLabel.setAlignment(Qt.AlignCenter)
        welcomeLabel.setGeometry(QRect(0, (self.height() - 100) // 10, screenSize.width() - 370, 100))
        font = QFont(font_family)
        font.setPointSize(75)
        font.setBold(True)
        welcomeLabel.setFont(font)

        # Buttons
        button1 = QPushButton("Daftar Buku", self)
        button1.setGeometry(QRect(70, 200, screenSize.width() // 3, 300))
        button1.setFont(font)

        # Set icon for button1
        icon1 = QIcon("../../assets/icons/book_icon.png")  # Replace with your icon path
        button1.setIcon(icon1)
        button1.setCheckable(True)
        button1.clicked.connect(lambda: self.whatsShowing.emit(1))
        button1.setIconSize(QSize(64, 64))  # Adjust icon size as needed
        button1.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green */
                border: none;
                color: white;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 28px;
                cursor: pointer;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton::icon {
                margin-bottom: 20px; /* Adjust icon margin as needed */
            }
        """)

        button2 = QPushButton("Daftar Anggota", self)
        button2.setGeometry(QRect(button1.width() + 10 + 70, 200, screenSize.width() // 3, 300))
        button2.setFont(font)

        # Set icon for button2
        icon2 = QIcon("../../assets/icons/person_icon.png")  # Replace with your icon path
        button2.setIcon(icon2)
        button2.setCheckable(True)
        button2.clicked.connect(lambda: self.whatsShowing.emit(2))
        button2.setIconSize(QSize(64, 64))  # Adjust icon size as needed
        button2.setStyleSheet("""
            QPushButton {
                background-color: #008CBA; /* Blue */
                border: none;
                color: white;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 28px;
                cursor: pointer;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #005F6B;
            }
            QPushButton::icon {
                margin-bottom: 20px; /* Adjust icon margin as needed */
            }
        """)

        self.setStyleSheet("""
            background-color: white;
            color: black;
        """)
