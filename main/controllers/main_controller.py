from PySide6.QtWidgets import QMainWindow, QTextEdit
from PySide6.QtGui import QFont
from functions.create_main_widget import create_main_widget
from icons import *
from themes import dark

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 500)
        self.initialTitle = "Untitled"
        self.setWindowTitle(self.initialTitle)
        self.current_path = None
        self.current_font_size = 14
        self.custom_font = QFont()
        self.custom_font.setPointSize(self.current_font_size)
        self.setStyleSheet(dark.darkThemeStyle)
        self.recentlyOpen = False
        self.text_edit = QTextEdit()
        self.text_edit.setViewportMargins(8, 6, 8, 8)
        self.text_edit.setFrameStyle(0)
        self.text_edit.setFont(self.custom_font)
        self.setCentralWidget(create_main_widget(self.text_edit))

if __name__ == "__main__":
    pass