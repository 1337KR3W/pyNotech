from PySide6.QtGui import QIcon

########################
# LIGHT THEME FUNCTION #
def setLightTheme(self):
    self.setStyleSheet("")
    self.zoomIn.setIcon(QIcon("resources/icons/zoomIn_icon.PNG"))
    self.zoomOut.setIcon(QIcon("resources/icons/zoomOut_icon.PNG"))
    self.copy.setIcon(QIcon("resources/icons/copy_icon.PNG"))
    self.cut.setIcon(QIcon("resources/icons/cut_icon.PNG"))
    self.paste.setIcon(QIcon("resources/icons/paste_icon.PNG"))
    self.contribute.setIcon(QIcon("resources/icons/github-mark.PNG"))
    self.undo.setIcon(self.undo_icon)
    self.redo.setIcon(self.redo_icon)
#---------------------------------------------------------------------------------------