from PySide6.QtWidgets import QMainWindow, QTextEdit, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont
from functions.create_main_widget import create_main_widget
from icons import *
from themes import dark
from ui.menu_bar.menu_bar import MenuBar

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
        #self.text_edit.textChanged.connect(self.updateWindowTitle)
        
        # MAIN WIDGET AND LAYOUT #
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # ADD WIDGETS FUNCTION #
        def add_widget(layout, widget):
            hbox = QHBoxLayout()
            hbox.addWidget(widget)
            layout.addLayout(hbox)

        add_widget(main_layout, self.text_edit)
        
        #self.setCentralWidget(create_main_widget(self.text_edit))

        # MENU BAR
        self.menuBar = MenuBar(self)
        self.setMenuBar(self.menuBar)
        

if __name__ == "__main__":
    pass