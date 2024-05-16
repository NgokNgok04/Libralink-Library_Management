# myapp.py
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My PySide6 App")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

        self.clicked = False

    def on_button_click(self):
        self.clicked = True
        self.message = "kontol"

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()