from PySide6.QtWidgets import QFileDialog

######################
# OPEN FILE FUNCTION #        
def openFile(self):
    open_file = QFileDialog().getOpenFileName(self, 'Open file', 'Desktop','Text files (*.txt)')
    if open_file:
        self.recentlyOpen = True
        try:
            self.initialTitle = open_file[0]
            self.setWindowTitle(self.initialTitle)
            #self.setWindowTitle(open_file[0])
            with open(open_file[0], 'r') as f:
                file_text = f.read()
                self.text_edit.setPlainText(file_text)
            self.current_path = open_file[0]
            self.recentlyOpen = False
        except FileNotFoundError:
            print("File not found")
    else:
        print("No file selected")