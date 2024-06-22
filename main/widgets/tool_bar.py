from PySide6.QtWidgets import QToolBar

class ToolBar:
    def __init__(self):

        # TOOL BAR #
        toolBar = QToolBar()
        toolBar.setMovable(False)
        self.addToolBar(toolBar)

        #---- TOOL BAR ADDED ACTIONS
        toolBar.addAction(self.new)
        toolBar.addAction(self.open)
        toolBar.addAction(self.save)
        toolBar.addSeparator()
        toolBar.addAction(self.search)
        toolBar.addAction(self.cleanSearch)