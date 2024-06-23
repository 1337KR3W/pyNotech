from PySide6.QtWidgets import QApplication, QStyle

class Icons:
    def __init__(self):
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication([])
        self.style = self.app.style()

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

    def appearance_icon(self):
        return self.get_standard_icon("SP_DesktopIcon")

    def undo_icon(self):
        return self.get_standard_icon("SP_MediaSeekBackward")

    def undo_icon_w(self):
        return self.get_standard_icon("SP_ArrowBack")

    def redo_icon(self):
        return self.get_standard_icon("SP_MediaSeekForward")

    def redo_icon_w(self):
        return self.get_standard_icon("SP_ArrowRight")

    def about_icon(self):
        return self.get_standard_icon("SP_FileDialogInfoView")

    def search_icon(self):
        return self.get_standard_icon("SP_FileDialogContentsView")

    def selectAll_icon(self):
        return self.get_standard_icon("SP_FileDialogDetailedView")

    def cleanSearch_icon(self):
        return self.get_standard_icon("SP_DialogResetButton")

    def help_icon(self):
        return self.get_standard_icon("SP_DialogHelpButton")