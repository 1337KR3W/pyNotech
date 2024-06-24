from main.functions.zoom_in_editor import zoomInEditor
from main.functions.zoom_out_editor import zoomOutEditor
from themes.dark import setDarkTheme
from themes.light import setLightTheme

class PreferencesConnections:
    def __init__(self, parent):
        self.parent = parent

        #---- Parameters CONNECTIONS
        self.parent.zoomIn.triggered.connect(self.zoomInEditor)
        self.parent.zoomOut.triggered.connect(self.zoomOutEditor)
        self.parent.darkTheme.triggered.connect(self.changeToDarkTheme)
        self.parent.lightTheme.triggered.connect(self.changeToLightTheme)
    
    
    def changeToDarkTheme(self):
        self.parent.setDarkTheme()

    def changeToLightTheme(self):
        self.parent.setLightTheme()

    