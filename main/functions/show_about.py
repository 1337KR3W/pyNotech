from PySide6.QtWidgets import QVBoxLayout, QLabel, QFrame, QDialog
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from icons.icons import Icons

#################
# ABOUT WINDOWN #
def showAbout(self):
    icons = Icons()
    about_icon = icons.about_icon()
    dialog = QDialog()
    dialog.setWindowTitle("About")
    dialog.setWindowIcon(about_icon)
    dialog.setModal(True)
    dialog.setStyleSheet("background-color: rgb(175,210,255)")
    aboutFont = QFont()
    aboutFont.setPointSize(11)
    # ABOUT LABEL #
    label = QLabel("      pyNotech es un bloc de notas digital desarrollado como proyecto open source para\n"+
                        "el trabajo de fin de grado en Ingeniería Informática del Software por la Universidad de\n"+
                        "Sevilla (US). Utilizando PySide6 para Python, pyNotech es una aplicación de escritorio\n"+
                        "intuitiva y eficiente, desarrollada con el objetivo de aprender y establecer las bases del\n"+
                        "desarrollo de aplicaciones de escritorio.\n\n\n"
                        "Autor, José Joaquín Rojas Romero                                                 pyNotech v1.0.0-beta")
    # ABOUT LABEL STYLE #
    label.setAlignment(Qt.AlignmentFlag.AlignJustify)
    label.setFont(aboutFont)
    label.setMargin(10)
    label.setStyleSheet("background-color: rgb(220,236,255);")#
    label.setFrameShape(QFrame.Panel)#
    label.setFrameShadow(QFrame.Sunken)#
    label.setLineWidth(2)#
    # LAYOUT #
    layout = QVBoxLayout()
    layout.addWidget(label)
    dialog.setLayout(layout)
    dialog.exec()
#---------------------------------------------------------------------------------------