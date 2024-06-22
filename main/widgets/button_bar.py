from PySide6.QtWidgets import QHBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt
from controllers.main_controller import MainWindow
from functions.update_info import updateInfo

class BottomBar:
    def __init__(self):
                
        ########################
        # BOTTON BAR WITH INFO #
        bottomLayout = QHBoxLayout()
        #---- DATE LABEL
        self.dateInfo = QLabel()
        #---- OS LABEL
        self.osTag = QLabel()
        #---- LANGUAJE LABEL
        self.langTag = QLabel()
        #---- UPDATE INFO CALL FUNCTION
        updateInfo()
        #---- ACTUAL HOVER INFO
        self.hoverInfo = QLabel()
        self.hoverInfo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        #---- SEPARATOR FOR TAGS
        separator1 = QFrame()
        separator1.setFrameShape(QFrame.VLine)
        separator1.setFrameShadow(QFrame.Sunken)
        separator2 = QFrame()
        separator2.setFrameShape(QFrame.VLine)
        separator2.setFrameShadow(QFrame.Sunken)
        #---- ADDING WIDGETS TO BOTTOM LAYOUT
        bottomLayout.addWidget(self.osTag)
        bottomLayout.addWidget(separator1)
        bottomLayout.addWidget(self.langTag)
        bottomLayout.addWidget(separator2)
        bottomLayout.addWidget(self.dateInfo)
        bottomLayout.addWidget(self.hoverInfo)
        bottomLayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        bottomLayout.setSpacing(15) 
        #---- ADDING BOTTOM LAYOUT TO MAIN LAYOUT
        MainWindow.main_layout.addLayout(bottomLayout)
        #---------------------------------------------------------------------------------------