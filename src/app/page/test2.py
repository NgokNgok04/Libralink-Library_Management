from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Table")
        self.tableWidget = QTableWidget(3, 3)
        self.setCentralWidget(self.tableWidget)

        # Add button to cell (1, 1)
        button = QPushButton("Click me")
        self.tableWidget.setCellWidget(1, 1, button)

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec()
