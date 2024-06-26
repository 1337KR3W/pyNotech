from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QFrame, QDialog, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

####################
# MORE HELP WINDOW #
def showMoreHelp(self):
    # MORE HELP DIALOG #
    dialog = QDialog()
    dialog.setWindowTitle("More help")
    dialog.setModal(True)
    dialog.setStyleSheet("background-color: rgb(175,210,255)")
    # TABLES CREATION #
    shortcutsTable1 = QTableWidget()
    shortcutsTable1.setColumnCount(2)    
    shortcutsTable1.setHorizontalHeaderLabels(["Shortcut", "Description"])
    shortcutsTable2 = QTableWidget()
    shortcutsTable2.setColumnCount(2)    
    shortcutsTable2.setHorizontalHeaderLabels(["Shortcut", "Description"])
    # DATA FOR TABLE 1 #
    shortcuts1 ={"New file": "Ctrl + N",
                    "Open file": "Ctrl + O",              
                    "Save file": "Ctrl + S",            
                    "Save file as": "Ctrl + Shift + S",     
                    "Exit": "Ctrl + Q",
                    "Zoom in": "Ctrl + +",             
                    "Zoom out": "Ctrl + -"}
    # DATA FOR TABLE 2 #
    shortcuts2 ={"Copy": "Ctrl + C",
                    "Cut": "Ctrl + X",
                    "Paste": "Ctrl + V",
                    "Search": "Ctrl + F",
                    "Select all": "Ctrl + A",
                    "Undo": "Ctrl + Z",
                    "Redo": "Ctrl + Y"}
    # SET ROWS #
    shortcutsTable1.setRowCount(len(shortcuts1))
    shortcutsTable2.setRowCount(len(shortcuts2))
    # TABLE 1 #
    for row, (description, shortcut) in enumerate(shortcuts1.items()):
        shortcutsTable1.setColumnWidth(1,154)
        shortcutsTable1.setItem(row, 0, QTableWidgetItem(description))
        shortcutsTable1.setItem(row, 1, QTableWidgetItem(shortcut))
    shortcutsTable1.verticalHeader().setVisible(False)  # Ocultar la cabecera vertical
    # TABLE 2 #
    for row, (description, shortcut) in enumerate(shortcuts2.items()):
        shortcutsTable2.setColumnWidth(1,154)
        shortcutsTable2.setItem(row, 0, QTableWidgetItem(description))
        shortcutsTable2.setItem(row, 1, QTableWidgetItem(shortcut))
    shortcutsTable2.verticalHeader().setVisible(False)  # Ocultar la cabecera vertical
    # TABLES STYLE #
    moreHelpFont = QFont()
    moreHelpFont.setPointSize(11)
    shortcutsTable1.setFont(moreHelpFont)
    shortcutsTable2.setFont(moreHelpFont)
    shortcutsTable1.setStyleSheet("background-color: rgb(220,236,255);")
    shortcutsTable2.setStyleSheet("background-color: rgb(220,236,255);")
    shortcutsTable1.setFrameShape(QFrame.Panel)
    shortcutsTable1.setFrameShadow(QFrame.Sunken)
    shortcutsTable1.setLineWidth(2)
    shortcutsTable2.setFrameShape(QFrame.Panel)
    shortcutsTable2.setFrameShadow(QFrame.Sunken)
    shortcutsTable2.setLineWidth(2)
    # CONTACT INFO LABEL #
    label = QLabel("Si usted encuentra algún problema con la aplicación puede ponerse en contacto\n"
                   "con nosotros mandando un email a la siguiente dirección de correo electrónico:\n\n\n"
                   "josrojrom1@alum.us.es")
    # CONTACT INFO STYLE #
    label.setAlignment(Qt.AlignmentFlag.AlignJustify)
    label.setFont(moreHelpFont)
    label.setMargin(10)
    label.setStyleSheet("background-color: rgb(220,236,255);")
    label.setFrameShape(QFrame.Panel)
    label.setFrameShadow(QFrame.Sunken)
    label.setLineWidth(2)
    # LAYOUTS #
    layout = QVBoxLayout()
    layoutH = QHBoxLayout()
    layoutH.addWidget(shortcutsTable1)
    layoutH.addWidget(shortcutsTable2)
    layout.addLayout(layoutH)
    layout.addWidget(label)
    dialog.setLayout(layout)
    dialog.exec()