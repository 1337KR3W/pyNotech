from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QFont

class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setViewportMargins(8, 6, 8, 8)
        self.setFrameStyle(0)
        self.custom_font = QFont()
        self.custom_font.setPointSize(14)
        self.setFont(self.custom_font)
        self.textChanged.connect(parent.update_window_title)