from PySide6.QtGui import QIcon

#######################
# DARK THEME FUNCTION #
def setDarkTheme(self):
    self.setStyleSheet(self.darkThemeStyle)
    self.zoomIn.setIcon(QIcon("resources/icons/zoomIn_icon_w.PNG"))
    self.zoomOut.setIcon(QIcon("resources/icons/zoomOut_icon_w.PNG"))
    self.copy.setIcon(QIcon("resources/icons/copy_icon_w.PNG"))
    self.cut.setIcon(QIcon("resources/icons/cut_icon_w.PNG"))
    self.paste.setIcon(QIcon("resources/icons/paste_icon_w.PNG"))
    self.contribute.setIcon(QIcon("resources/icons/github-mark-white.PNG"))
    self.undo.setIcon(self.undo_icon_w)
    self.redo.setIcon(self.redo_icon_w)
#---------------------------------------------------------------------------------------