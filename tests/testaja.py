# test_myapp.py
import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from src.app.App import App

@pytest.fixture
def app(qtbot):
    test_app = QApplication.instance()
    if test_app is None:
        test_app = QApplication([])

    window = App()
    qtbot.addWidget(window)
    window.show()
    return window

def test_button_click(qtbot, app):
    # Check initial state
    assert not app.clicked

    # Simulate button click
    qtbot.mouseClick(app.button, Qt.LeftButton)

    # Check final state
    assert app.clicked

def test_button_clicked(qtbot,app):
    assert not app.clicked

    # Simulate button click
    qtbot.mouseClick(app.button, Qt.LeftButton)

    # Check final state
    assert app.clicked
    assert app.message == "KONTOL"