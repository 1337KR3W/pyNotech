from PySide6.QtWidgets import QMenu, QWidgetAction
from icons.icons import Icons

class FileMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        icons = Icons()
        new_icon = icons.new_icon()
        open_icon = icons.open_icon()
        save_icon = icons.save_icon()
        exit_icon = icons.exit_icon()
        self.setTitle("File")
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
        #------------------------- SAVE AS ACTION
        self.saveAs = QWidgetAction(self)
        self.saveAs.setIcon(save_icon)
        self.saveAs.setShortcut("Ctrl+Shift+S")
        self.saveAs.setIconText("Save as...")
        self.addAction(self.saveAs)
        #------------------------- EXIT ACTION
        self.exit = QWidgetAction(self)
        self.exit.setIcon(exit_icon)
        self.exit.setShortcut("Ctrl+Q")
        self.exit.setIconText("Exit")
        self.addAction(self.exit)

 


