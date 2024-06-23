from PySide6.QtWidgets import QHBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt, QTimer
from datetime import *
import platform
import locale

class BottomBar(QHBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)
        #---- DATE LABEL
        self.dateInfo = QLabel()
        #---- OS LABEL
        self.osTag = QLabel()
        #---- LANGUAJE LABEL
        self.langTag = QLabel()
        #---- UPDATE INFO CALL FUNCTION
        self.updateInfo()
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
        self.addWidget(self.osTag)
        self.addWidget(separator1)
        self.addWidget(self.langTag)
        self.addWidget(separator2)
        self.addWidget(self.dateInfo)
        self.addWidget(self.hoverInfo)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setSpacing(15) 
    ####################################
    # UPDATE BOTTOM LAYOUT DATA LABELS #
    def updateInfo(self):
        # DATE LABEL DATA
        self.dateInfo.setText(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateInfo)
        self.timer.start(1000)
        # OS LABEL DATA
        system = platform.system()
        release = platform.release()
        self.osTag.setText(f"{system} {release}")
        # LANGUAJE LABEL DATA
        language, _ = locale.getlocale()
        self.langTag.setText(f"{language}")
    #---------------------------------------------------------------------------------------    
        
        #---------------------------------------------------------------------------------------