from PySide6.QtWidgets import QStyle
from PySide6.QtWidgets import QApplication

#---- ICONS, Uncoment and iterate for getting all posible icons
#icons = sorted([attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")])
#------------------------- NEW ICON
new_icon_path = getattr(QStyle, "SP_FileIcon")
new_icon = QApplication.style().standardIcon(new_icon_path)
#------------------------- OPEN ICON
open_icon_path = getattr(QStyle, "SP_DirClosedIcon")
open_icon = QApplication.style().standardIcon(open_icon_path)
#------------------------- SAVE ICON
save_icon_path = getattr(QStyle, "SP_DialogSaveButton")
save_icon = QApplication.style().standardIcon(save_icon_path)
#------------------------- EXIT ICON
exit_icon_path = getattr(QStyle, "SP_DialogCancelButton")
exit_icon = QApplication.style().standardIcon(exit_icon_path)
#------------------------- APPEARANCE ICON
appearance_icon_path = getattr(QStyle, "SP_DesktopIcon")
appearance_icon = QApplication.style().standardIcon(appearance_icon_path)
#------------------------- UNDO ICON
undo_icon_path = getattr(QStyle, "SP_MediaSeekBackward")
undo_icon = QApplication.style().standardIcon(undo_icon_path)    
#------------------------- REDO ICON
redo_icon_path = getattr(QStyle, "SP_MediaSeekForward")
redo_icon = QApplication.style().standardIcon(redo_icon_path)             
#------------------------- UNDO WHITE ICON
undo_icon_w_path = getattr(QStyle, "SP_ArrowBack")
undo_icon_w = QApplication.style().standardIcon(undo_icon_w_path)    
#------------------------- REDO WHITE ICON
redo_icon_w_path = getattr(QStyle, "SP_ArrowRight")
redo_icon_w = QApplication.style().standardIcon(redo_icon_w_path) 
#------------------------- ABOUT ICON
about_icon_path = getattr(QStyle, "SP_FileDialogInfoView")
about_icon = QApplication.style().standardIcon(about_icon_path) 
#------------------------- SEARCH ICON
search_icon_path = getattr(QStyle, "SP_FileDialogContentsView")
search_icon = QApplication.style().standardIcon(search_icon_path)
#------------------------- SEARCH ICON
selectAll_icon_path = getattr(QStyle, "SP_FileDialogDetailedView")
selectAll_icon = QApplication.style().standardIcon(selectAll_icon_path)
#------------------------- CLEAN SEARCH ICON
cleanSearch_icon_path = getattr(QStyle, "SP_DialogResetButton")
cleanSearch_icon = QApplication.style().standardIcon(cleanSearch_icon_path)   
#------------------------- HELP ICON
help_icon_path = getattr(QStyle, "SP_DialogHelpButton")
help_icon = QApplication.style().standardIcon(help_icon_path)  
#---------------------------------------------------------------------------------------