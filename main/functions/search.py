from PySide6.QtWidgets import QInputDialog
from PySide6.QtGui import QTextCursor, QBrush, QTextCharFormat, QColor
from PySide6.QtCore import QRegularExpression

#####################
# SEARCH FUNCTION #
def searchAndHighlight(self):
    pattern, ok = QInputDialog.getText(self, "Search", "Enter your search term:")   
    if ok:
        cursor = self.text_edit.textCursor()
        # FORMAT MATCHES COLORING #
        format = QTextCharFormat()
        format.setBackground(QBrush(QColor("yellow")))
        self.menuBar.editMenu.cleanSearch.setDisabled(False)
        # REGEX SETUP #
        re = QRegularExpression(pattern)
        # REGULAR EXPRESSION MATCH ITERATOR #
        i = re.globalMatch(self.text_edit.toPlainText())

        # ITERATE THROUGH ALL THE MATCHES AND HIGHLIGHT
        while i.hasNext():
            # REGULAR EXPRESSION MATCH
            match = i.next()

            # FORMATING OF MATCHED TEXT
            cursor.setPosition(match.capturedStart(), QTextCursor.MoveAnchor)
            cursor.setPosition(match.capturedEnd(), QTextCursor.KeepAnchor)
            cursor.mergeCharFormat(format)