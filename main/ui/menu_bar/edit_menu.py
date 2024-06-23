from PySide6.QtWidgets import QMenu, QWidgetAction
from PySide6.QtGui import QIcon
from icons.icons import Icons
import os

class EditMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        icons = Icons()
        undo_icon =icons.undo_icon()
        redo_icon = icons.redo_icon()
        search_icon = icons.search_icon()
        selectAll_icon = icons.selectAll_icon()
        cleanSearch_icon = icons.cleanSearch_icon() 
        self.setTitle("Edit")
        main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

        #------------------------- COPY ACTION
        self.copy = QWidgetAction(self)  
        self.copy.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'copy_icon.PNG')))
        self.copy.setShortcut("Ctrl+C")
        self.copy.setIconText("Copy")
        self.addAction(self.copy)
        #------------------------- CUT ACTION
        self.cut = QWidgetAction(self)
        self.cut.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'cut_icon.PNG')))
        self.cut.setShortcut("Ctrl+X")
        self.cut.setIconText("Cut")
        self.addAction(self.cut)
        #------------------------- PASTE ACTION
        self.paste = QWidgetAction(self)
        self.paste.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'paste_icon.PNG')))
        self.paste.setShortcut("Ctrl+V")
        self.paste.setIconText("Paste")
        self.addAction(self.paste)
        self.addSeparator()
        #------------------------- SELECT ALL ACTION
        self.selectAll = QWidgetAction(self)
        self.selectAll.setIcon(selectAll_icon)
        self.selectAll.setShortcut("Ctrl+A")
        self.selectAll.setIconText("Select all")
        self.addAction(self.selectAll)
        #------------------------- SEARCH ACTION
        self.search = QWidgetAction(self)
        self.search.setIcon(search_icon)
        self.search.setShortcut("Ctrl+F")
        self.search.setIconText("Search")
        self.addAction(self.search)
        #------------------------- CLEAN SEARCH ACTION
        self.cleanSearch = QWidgetAction(self)
        self.cleanSearch.setIcon(cleanSearch_icon)
        self.cleanSearch.setShortcut("Ctrl+B")
        self.cleanSearch.setIconText("Clean search")
        self.cleanSearch.setDisabled(True)
        self.addAction(self.cleanSearch)
        self.addSeparator()
        #------------------------- UNDO ACTION
        self.undo = QWidgetAction(self)
        self.undo.setIcon(undo_icon)
        self.undo.setShortcut("Ctrl+Z")
        self.undo.setIconText("Undo")
        self.addAction(self.undo)
        #------------------------- REDO ACTION
        self.redo = QWidgetAction(self)
        self.redo.setIcon(redo_icon)
        self.redo.setShortcut("Ctrl+Y")
        self.redo.setIconText("Redo")
        self.addAction(self.redo)