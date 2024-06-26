from PySide6.QtWidgets import QApplication, QStyle
from PySide6.QtGui import QIcon
import os

class Icons:
    def __init__(self):
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication([])
        self.style = self.app.style()
        self.main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def get_standard_icon(self, icon_path):
        return self.style.standardIcon(getattr(QStyle, icon_path))

    def new_icon(self):
        return self.get_standard_icon("SP_FileIcon")

    def open_icon(self):
        return self.get_standard_icon("SP_DirClosedIcon")

    def save_icon(self):
        return self.get_standard_icon("SP_DialogSaveButton")

    def exit_icon(self):
        return self.get_standard_icon("SP_DialogCancelButton")
    
    def copy_icon(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'copy_icon.PNG'))
    
    def copy_icon_w(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'copy_icon_W.PNG'))
    
    def cut_icon(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'cut_icon.PNG'))
    
    def cut_icon_w(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'cut_icon_w.PNG'))

    def paste_icon(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'paste_icon.PNG'))
    
    def paste_icon_w(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'paste_icon_w.PNG'))

    def undo_icon(self):
        return self.get_standard_icon("SP_MediaSeekBackward")

    def undo_icon_w(self):
        return self.get_standard_icon("SP_ArrowBack")

    def redo_icon(self):
        return self.get_standard_icon("SP_MediaSeekForward")

    def redo_icon_w(self):
        return self.get_standard_icon("SP_ArrowRight")

    def search_icon(self):
        return self.get_standard_icon("SP_FileDialogContentsView")

    def selectAll_icon(self):
        return self.get_standard_icon("SP_FileDialogDetailedView")

    def cleanSearch_icon(self):
        return self.get_standard_icon("SP_DialogResetButton")
    
    def zoomIn_icon(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'zoomIn_icon.PNG'))
    
    def zoomIn_icon_w(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'zoomIn_icon_w.PNG'))
    
    def zoomOut_icon(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'zoomOut_icon.PNG'))

    def zoomOut_icon_w(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'zoomOut_icon_w.PNG'))

    def appearance_icon(self):
        return self.get_standard_icon("SP_DesktopIcon")

    def help_icon(self):
        return self.get_standard_icon("SP_DialogHelpButton")
    
    def about_icon(self):
        return self.get_standard_icon("SP_FileDialogInfoView")
    
    def contribute_icon(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'github-mark.PNG'))
    
    def contribute_icon_w(self):
        return QIcon(os.path.join(self.main_dir, 'resources', 'icons', 'github-mark-white.PNG'))