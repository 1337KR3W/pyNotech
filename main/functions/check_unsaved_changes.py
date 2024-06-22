from PySide6.QtWidgets import QMessageBox

################################################
# CHECKING SAVE STATUS BEFORE EXITING FUNCTION #
def checkUnsaveChanges(self):
    self.saved_changes = False
    if self.text_edit.toPlainText():
        reply = QMessageBox.question(self, 'Unsaved changes', '¿Do you want to save your changes before exiting?', QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        # WHEN SAVE IS PRESSED #
        if reply == QMessageBox.Save:
            self.saveFile()
            self.text_edit.setPlainText('')
            self.close()
        # WHEN DISCARD IS PRESSED #
        elif reply == QMessageBox.Discard:
            self.text_edit.setPlainText('')
            self.close()
        # WHEN CANCEL IS PRESSED #
        else:
            pass
    else:
        self.close()  
#---------------------------------------------------------------------------------------