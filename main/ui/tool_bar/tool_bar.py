from PySide6.QtWidgets import QToolBar, QWidgetAction
from icons.icons import Icons

class ToolBar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        icons = Icons()
        new_icon = icons.new_icon()
        open_icon = icons.open_icon()
        save_icon = icons.save_icon()
        search_icon = icons.search_icon()
        cleanSearch_icon = icons.cleanSearch_icon()

        # TOOL BAR
        self.setMovable(False)

        #------------------------- NEW ACTION
        self.new = QWidgetAction(self)  
        self.new.setIcon(new_icon)
        self.new.setShortcut("Ctrl+N")
        self.new.setIconText("New")
        self.addAction(self.new)
        #------------------------- OPEN ACTION
        self.open = QWidgetAction(self)
        self.open.setIcon(open_icon)
        self.open.setShortcut("Ctrl+O")
        self.open.setIconText("Open")
        self.addAction(self.open)
        #------------------------- SAVE ACTION
        self.save = QWidgetAction(self)
        self.save.setIcon(save_icon)
        self.save.setShortcut("Ctrl+S")
        self.save.setIconText("Save")
        self.addAction(self.save)

        self.addSeparator()

        self.search_action = QWidgetAction(self)
        self.search_action.setIcon(search_icon)
        self.search_action.setShortcut("Ctrl+F")
        self.search_action.setIconText("Search")
        self.addAction(self.search_action)

        self.cleanSearch = QWidgetAction(self)
        self.cleanSearch.setIcon(cleanSearch_icon)
        self.cleanSearch.setShortcut("Ctrl+B")
        self.cleanSearch.setIconText("Clean search")
        self.cleanSearch.setDisabled(True)
        self.addAction(self.cleanSearch)
        self.show()