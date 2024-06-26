from PySide6.QtWidgets import QMenuBar
from ui.menu_bar.file_menu import FileMenu
from ui.menu_bar.edit_menu import EditMenu
from ui.menu_bar.preferences_menu import PreferencesMenu
from ui.menu_bar.help_menu import HelpMenu

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #----------------------------------- FILE MENU BAR OPTION
        self.fileMenu = FileMenu(self)
        self.addMenu(self.fileMenu)
        #----------------------------------- EDIT MENU BAR OPTION
        self.editMenu = EditMenu(self)
        self.addMenu(self.editMenu)
        #----------------------------------- PREFERENCES MENU BAR OPTION
        self.preferencesMenu = PreferencesMenu(self.parent)
        self.addMenu(self.preferencesMenu)
        #----------------------------------- HELP MENU BAR OPTION
        self.helpMenu = HelpMenu(self)
        self.addMenu(self.helpMenu)