from PySide6.QtWidgets import QFileDialog
#########################
# SAVE FILE AS FUNCTION #
def saveFileAs(self):
    pathName = QFileDialog.getSaveFileName(self, 'Save file', '', 'Text files (*.txt)')
    fileTextContent = self.text_edit.toPlainText()
    with open(pathName[0], 'w') as f:
        f.write(fileTextContent)
    self.current_path = pathName[0]
    self.initialTitle = pathName[0]
    self.setWindowTitle(pathName[0])               
#---------------------------------------------------------------------------------------