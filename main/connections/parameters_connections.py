class ParametersConnections:
    def __init__(self):

        #---- Parameters CONNECTIONS
        self.zoomIn.triggered.connect(self.zoomInEditor)
        self.zoomOut.triggered.connect(self.zoomOutEditor)
        self.darkTheme.triggered.connect(self.setDarkTheme)
        self.lightTheme.triggered.connect(self.setLightTheme)