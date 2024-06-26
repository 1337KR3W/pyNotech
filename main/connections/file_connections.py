def setup_file_connections(main_window):
    main_window.menuBar.fileMenu.save.triggered.connect(main_window.save_file)
    main_window.menuBar.fileMenu.saveAs.triggered.connect(main_window.save_file_as)
    main_window.menuBar.fileMenu.open.triggered.connect(main_window.open_file)
    main_window.menuBar.fileMenu.new.triggered.connect(main_window.new_file)
    

'''
class FileConnections:
    def __init__(self):
        #---- File CONNECTIONS
        self.new.triggered.connect(self.newFile)
        self.open.triggered.connect(self.openFile)
        self.save.triggered.connect(self.saveFile)
        self.saveAs.triggered.connect(self.saveFileAs)
        self.exit.triggered.connect(self.checkUnsaveChanges)
'''