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
        # TOOL BAR SETTINGS
        self.setMovable(True)
        #------------------------- NEW ACTION
        self.new = QWidgetAction(self)  
        self.new.setIcon(new_icon)
        self.new.setIconText("New")
        self.addAction(self.new)
        #------------------------- OPEN ACTION
        self.open = QWidgetAction(self)
        self.open.setIcon(open_icon)
        self.open.setIconText("Open")
        self.addAction(self.open)
        #------------------------- SAVE ACTION
        self.save = QWidgetAction(self)
        self.save.setIcon(save_icon)
        self.save.setIconText("Save")
        self.addAction(self.save)

        self.addSeparator()

        self.search_action = QWidgetAction(self)
        self.search_action.setIcon(search_icon)
        self.search_action.setIconText("Search")
        self.addAction(self.search_action)

        self.cleanSearch = QWidgetAction(self)
        self.cleanSearch.setIcon(cleanSearch_icon)
        self.cleanSearch.setIconText("Clean search")
        self.cleanSearch.setDisabled(True)
        self.addAction(self.cleanSearch)
        # CONNECTIONS #
        self.save.triggered.connect(parent.save_file)
        self.open.triggered.connect(parent.open_file)