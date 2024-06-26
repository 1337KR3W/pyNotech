from PySide6.QtWidgets import QMenu, QWidgetAction
from icons.icons import Icons

class PreferencesMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        icons = Icons()
        appearance_icon = icons.appearance_icon()
        zoomIn_icon = icons.zoomIn_icon()
        zoomOut_icon = icons.zoomOut_icon()
        self.setTitle("Preferences")
        #------------------------- ZOOM IN ACTION
        self.zoomIn = QWidgetAction(self)
        self.zoomIn.setIcon(zoomIn_icon)
        self.zoomIn.setShortcut("Ctrl++")
        self.zoomIn.setIconText("Zoom In")
        self.addAction(self.zoomIn)
        #------------------------- ZOOM OUT ACTION
        self.zoomOut = QWidgetAction(self)
        self.zoomOut.setIcon(zoomOut_icon)
        self.zoomOut.setShortcut("Ctrl+-")
        self.zoomOut.setIconText("Zoom Out")
        self.addAction(self.zoomOut)
        #------------------------- APPEARANCE SELECT ACTION
        self.appearance = self.addMenu('Appearance')
        self.appearance.setIcon(appearance_icon)
        #------------------------- DARK THEME 
        self.darkTheme = QWidgetAction(self)
        self.darkTheme.setIconText("Dark mode")
        self.appearance.addAction(self.darkTheme)
        #------------------------- LIGHT THEME
        self.lightTheme = QWidgetAction(self)
        self.lightTheme.setIconText("Light mode")
        self.appearance.addAction(self.lightTheme)
        # CONNECTIONS #
        self.darkTheme.triggered.connect(parent.changeToDarkTheme)
        self.lightTheme.triggered.connect(parent.changeToLightTheme)
        self.zoomIn.triggered.connect(parent.zoom_in)
        self.zoomOut.triggered.connect(parent.zoom_out)
        
