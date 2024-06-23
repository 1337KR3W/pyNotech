from PySide6.QtWidgets import QMenuBar
from ui.menu_bar.file_menu import FileMenu
from ui.menu_bar.edit_menu import EditMenu
from ui.menu_bar.preferences_menu import PreferencesMenu
from ui.menu_bar.help_menu import HelpMenu

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        # FILE MENU BAR OPTION
        fileMenu = FileMenu(self)
        self.addMenu(fileMenu)

        # EDIT MENU BAR OPTION
        editMenu = EditMenu(self)
        self.addMenu(editMenu)

        # PREFERENCES MENU BAR OPTION
        preferencesMenu = PreferencesMenu(self)
        self.addMenu(preferencesMenu)

        # HELP MENU BAR OPTION
        helpMenu = HelpMenu(self)
        self.addMenu(helpMenu)

        self.show()