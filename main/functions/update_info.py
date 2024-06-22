from PySide6.QtCore import QTimer
from datetime import *
import platform
import locale

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