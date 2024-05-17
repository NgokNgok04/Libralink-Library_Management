from PySide6.QtCore import QRect
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QGraphicsDropShadowEffect, QWidget, QVBoxLayout, QPushButton

app = QApplication([])

window = QWidget()
window.setGeometry(QRect(100, 100, 400, 300))  # Set the size and position of the window
window.setStyleSheet(u"background-color: white;")
layout = QVBoxLayout(window)
button = QPushButton("Click Me")
layout.addWidget(button)

shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(20)
shadow.setColor(QColor(0, 0, 0, 160))  # Semi-transparent black
shadow.setOffset(10, 10)  # Offset for X and Y

button.setGraphicsEffect(shadow)

window.show()
app.exec()