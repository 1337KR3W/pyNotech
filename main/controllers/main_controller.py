from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ########################
        # MAIN WINDOW SETTINGS #
        self.resize(800, 500)
        self.initialTitle = "Untitled"
        self.setWindowTitle(self.initialTitle)
        self.current_path = None
        self.current_font_size = 14
        self.custom_font = QFont()
        self.custom_font.setPointSize(self.current_font_size)
        self.darkThemeStyle = '''QWidget{background-color: rgb(49,49,49);color: #FFFFFF;}QTextEdit{background-color: rgb(29,29,29);}QMenuBar::item:selected{color: #000000;}QMenu::item:selected{background-color: rgb(66,66,66);}'''
        self.recentlyOpen = False
        #---------------------------------------------------------------------------------------
        ##########################
        # MAIN WIDGET AND LAYOUT #
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        #---------------------------------------------------------------------------------------
        
        ########################
        # ADD WIDGETS FUNCTION #
        def add_widget(layout, widget):
            hbox = QHBoxLayout()
            hbox.addWidget(widget)
            layout.addLayout(hbox)
        #---------------------------------------------------------------------------------------