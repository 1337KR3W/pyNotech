class FileConnections:
    def __init__(self):
        #---- File CONNECTIONS
        self.new.triggered.connect(self.newFile)
        self.open.triggered.connect(self.openFile)
        self.save.triggered.connect(self.saveFile)
        self.saveAs.triggered.connect(self.saveFileAs)
        self.exit.triggered.connect(self.checkUnsaveChanges)