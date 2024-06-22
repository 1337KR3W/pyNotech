######################
# SAVE FILE FUNCTION #
def saveFile(self):
    if self.current_path is not None:
        fileTextContent = self.text_edit.toPlainText()
        with open(self.current_path, 'w') as f:
            f.write(fileTextContent)
            self.initialTitle = str(self.current_path)
            self.setWindowTitle(self.initialTitle)
    else:
        self.saveFileAs()