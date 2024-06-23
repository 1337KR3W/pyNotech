from PySide6.QtWidgets import QMenu, QWidgetAction
from PySide6.QtGui import QIcon
from icons.icons import Icons

class HelpMenu(QMenu):
    def __init__(self, parent):
        super().__init__(parent)
        icons = Icons()
        about_icon = icons.about_icon()
        help_icon = icons.help_icon()
        self.setTitle("Help")

        #------------------------- ABOUT ACTION
        self.about = QWidgetAction(self)
        self.about.setIcon(about_icon)
        self.about.setIconText("About")
        self.addAction(self.about)
        #------------------------- CONTRIBUTE ACTION
        self.contribute = QWidgetAction(self)
        self.contribute.setIcon(QIcon("../../resources/icons/github-mark.PNG"))
        self.contribute.setIconText("Contribute")
        self.addAction(self.contribute)
        #------------------------- MORE HELP ACTION
        self.moreHelp = QWidgetAction(self)
        self.moreHelp.setIcon(help_icon)
        self.moreHelp.setIconText("More help...")
        self.addAction(self.moreHelp)

