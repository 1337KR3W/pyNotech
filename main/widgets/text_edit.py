from PySide6.QtWidgets import QTextEdit
from controllers.main_controller import MainWindow
from functions import update_window_title

class TextEdit:
    def __init__(self):
        ###############
        # TEXT EDITOR #
        self.text_edit = QTextEdit()
        self.text_edit.setViewportMargins(8, 6, 8, 8)
        self.text_edit.setFrameStyle(0)
        self.text_edit.setFont(MainWindow.custom_font)
        MainWindow.add_widget(MainWindow.main_layout, self.text_edit)
        self.text_edit.textChanged.connect(update_window_title.updateWindowTitle)
        #---------------------------------------------------------------------------------------