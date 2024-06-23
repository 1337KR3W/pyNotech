from PySide6.QtWidgets import QToolBar
from icons.icons import new_icon, open_icon, save_icon, search_icon

class ToolBar:
    def __init__(self):

        # TOOL BAR #
        tool_bar = QToolBar(self)
        tool_bar.setMovable(False)
        tool_bar.addAction("New", new_icon, "Ctrl+N")
        tool_bar.addAction("Open", open_icon, "Ctrl+O")
        tool_bar.addAction("Save", save_icon, "Ctrl+S")
        tool_bar.addSeparator()
        tool_bar.addAction("Search", search_icon, "Ctrl+F")
        tool_bar.addAction("Clean")
        