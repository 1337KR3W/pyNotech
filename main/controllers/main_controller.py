from PySide6.QtWidgets import QMainWindow, QTextEdit, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QFont
from ui.menu_bar.menu_bar import MenuBar
from ui.tool_bar.tool_bar import ToolBar
from ui.bottom_bar.botton_bar import BottomBar
from themes.theme_manager import ThemeManager
from functions.save_file import saveFile
from functions.save_file_as import saveFileAs
from connections.file_connections import setup_file_connections


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #----------------------------------- MAIN WINDOW SETTINGS 
        self.resize(800, 500)
        self.initialTitle = "Untitled"
        self.setWindowTitle(self.initialTitle)
        self.current_path = None
        self.current_font_size = 14
        self.custom_font = QFont()
        self.custom_font.setPointSize(self.current_font_size)
        self.recentlyOpen = False
        #----------------------------------- MAIN WIDGET AND LAYOUT 
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        #----------------------------------- ADD WIDGETS FUNCTION
        def add_widget(layout, widget):
            hbox = QHBoxLayout()
            hbox.addWidget(widget)
            layout.addLayout(hbox)
        #----------------------------------- TEXT EDITOR 
        self.text_edit = QTextEdit()
        self.text_edit.setViewportMargins(8, 6, 8, 8)
        self.text_edit.setFrameStyle(0)
        self.text_edit.setFont(self.custom_font)
        #self.text_edit.textChanged.connect(self.updateWindowTitle)
        add_widget(main_layout, self.text_edit)
        #----------------------------------- MENU BAR
        self.menuBar = MenuBar(self)
        self.setMenuBar(self.menuBar)
        #----------------------------------- TOOL BAR
        self.toolBar = ToolBar(self)
        self.addToolBar(self.toolBar)
        #----------------------------------- BOTTOM BAR
        self.bottomBar = BottomBar(self)
        main_layout.addLayout(self.bottomBar)
        #----------------------------------- CONNECTIONS
        setup_file_connections(self)
        #----------------------------------- THEMES 
        self.theme_manager = ThemeManager(
            self,             
            self.menuBar.editMenu,
            self.menuBar.preferencesMenu,
            self.menuBar.helpMenu
        ) 
        self.theme_manager.set_light_theme() # Default Light theme  
    # Dark theme call function            
    def changeToDarkTheme(self):
        self.theme_manager.set_dark_theme()
    # Light theme call function
    def changeToLightTheme(self):
        self.theme_manager.set_light_theme()
    # Save file call
    def save_file(self):
        saveFile(self)
    # Save file as call
    def save_file_as(self):
        saveFileAs(self)

