############################################
# CHECKING "X" BUTTON FROM WINDOW FUNCTION #
def closeEvent(self, event):
    if self.text_edit.toPlainText():
        self.checkUnsaveChanges()
        event.ignore()
    else:
        self.close
        event.accept()
#---------------------------------------------------------------------------------------