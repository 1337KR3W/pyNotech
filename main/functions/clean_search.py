from PySide6.QtGui import QTextCursor, QTextCharFormat

#################################
# CLEAN MATCHES BEFORE SEARCHING#
def cleanSearchTerms(self):
    cursor = self.text_edit.textCursor()
    cursor.select(QTextCursor.Document)
    format = QTextCharFormat()
    format.setFontUnderline(False)
    cursor.setCharFormat(format)
    self.text_edit.setFont(self.custom_font)
    self.menuBar.editMenu.cleanSearch.setDisabled(True)
    self.toolBar.cleanSearch.setDisabled(True)
#---------------------------------------------------------------------------------------