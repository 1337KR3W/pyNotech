##########################################
# ADD MARK IN THE TITLE WHEN NEW CHANGES #
def updateWindowTitle(self):
    if self.text_edit.textChanged and not self.recentlyOpen:
        self.setWindowTitle(f"{self.initialTitle} (*)")
    else:
        self.setWindowTitle(self.initialTitle)
#---------------------------------------------------------------------------------------