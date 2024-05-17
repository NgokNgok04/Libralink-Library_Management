import sys
from PySide6.QtWidgets import QApplication
from App import App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = App()
    ui.show()
    sys.exit(app.exec())