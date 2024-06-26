from PySide6.QtGui import QFont
from icons.icons import Icons

class WindowSettings:
    def __init__(self):
        # MAIN WINDOW SETTINGS
        icons = Icons()
        self.pynotech_icon = icons.pynotech_icon()
        self.resize = (800, 500)
        self.initial_title = "Untitled"
        self.current_path = None
        self.current_font_size = 14
        self.custom_font = QFont()
        self.custom_font.setPointSize(self.current_font_size)
        self.recently_open = False