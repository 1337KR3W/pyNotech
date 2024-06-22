from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl

############################
# CONTRIBUTE LINK FUNCTION #
def goGitRepo(self):
    url = QUrl("https://github.com/josrojrom1/pyNotech")
    QDesktopServices.openUrl(url)
#---------------------------------------------------------------------------------------