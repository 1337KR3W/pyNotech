from PySide6.QtWidgets import QMenu, QWidgetAction
from PySide6.QtGui import QIcon
from icons.icons import Icons

class PreferencesMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        icons = Icons()
        appearance_icon = icons.appearance_icon()
        self.setTitle("Preferences")

        #------------------------- ZOOM IN ACTION
        self.zoomIn = QWidgetAction(self)
        self.zoomIn.setIcon(QIcon("../../resources/icons/zoomIn_icon.PNG"))
        self.zoomIn.setShortcut("Ctrl++")
        self.zoomIn.setIconText("Zoom In")
        self.addAction(self.zoomIn)
        #------------------------- ZOOM OUT ACTION
        self.zoomOut = QWidgetAction(self)
        self.zoomOut.setIcon(QIcon("../../resources/icons/zoomOut_icon.PNG"))
        self.zoomOut.setShortcut("Ctrl+-")
        self.zoomOut.setIconText("Zoom Out")
        self.addAction(self.zoomOut)
        #------------------------- APPEARANCE SELECT ACTION
        self.appearance = QWidgetAction(self)
        self.appearance.setIcon(appearance_icon)
        self.appearance.setIconText("Appearance")
        self.addAction(self.appearance)
        #------------------------- DARK THEME 
        self.darkTheme = QWidgetAction(self)
        self.darkTheme.setIconText("Dark mode")
        #------------------------- LIGHT THEME
        self.lightTheme = QWidgetAction(self)
        self.lightTheme.setIconText("Light mode")
        #--------------- APPEARANCE SELECT OPTION
        self.appearance = self.addMenu('Appearance')
        self.appearance.addAction(self.darkTheme)
        self.appearance.addAction(self.lightTheme)