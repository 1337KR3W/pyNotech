from PySide6.QtWidgets import QStyle

class Icons:
    def __init__(self):
        #---- ICONS, Uncoment and iterate for getting all posible icons
        #icons = sorted([attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")])
        #------------------------- NEW ICON
        new_icon_path = getattr(QStyle, "SP_FileIcon")
        self.new_icon = self.style().standardIcon(new_icon_path)
        #------------------------- OPEN ICON
        open_icon_path = getattr(QStyle, "SP_DirClosedIcon")
        self.open_icon = self.style().standardIcon(open_icon_path)
        #------------------------- SAVE ICON
        save_icon_path = getattr(QStyle, "SP_DialogSaveButton")
        self.save_icon = self.style().standardIcon(save_icon_path)
        #------------------------- EXIT ICON
        exit_icon_path = getattr(QStyle, "SP_DialogCancelButton")
        self.exit_icon = self.style().standardIcon(exit_icon_path)
        #------------------------- APPEARANCE ICON
        appearance_icon_path = getattr(QStyle, "SP_DesktopIcon")
        self.appearance_icon = self.style().standardIcon(appearance_icon_path)
        #------------------------- UNDO ICON
        undo_icon_path = getattr(QStyle, "SP_MediaSeekBackward")
        self.undo_icon = self.style().standardIcon(undo_icon_path)    
        #------------------------- REDO ICON
        redo_icon_path = getattr(QStyle, "SP_MediaSeekForward")
        self.redo_icon = self.style().standardIcon(redo_icon_path)             
        #------------------------- UNDO WHITE ICON
        undo_icon_w_path = getattr(QStyle, "SP_ArrowBack")
        self.undo_icon_w = self.style().standardIcon(undo_icon_w_path)    
        #------------------------- REDO WHITE ICON
        redo_icon_w_path = getattr(QStyle, "SP_ArrowRight")
        self.redo_icon_w = self.style().standardIcon(redo_icon_w_path) 
        #------------------------- ABOUT ICON
        about_icon_path = getattr(QStyle, "SP_FileDialogInfoView")
        self.about_icon = self.style().standardIcon(about_icon_path) 
        #------------------------- SEARCH ICON
        search_icon_path = getattr(QStyle, "SP_FileDialogContentsView")
        self.search_icon = self.style().standardIcon(search_icon_path)
        #------------------------- SEARCH ICON
        selectAll_icon_path = getattr(QStyle, "SP_FileDialogDetailedView")
        self.selectAll_icon = self.style().standardIcon(selectAll_icon_path)
        #------------------------- CLEAN SEARCH ICON
        cleanSearch_icon_path = getattr(QStyle, "SP_DialogResetButton")
        self.cleanSearch_icon = self.style().standardIcon(cleanSearch_icon_path)   
        #------------------------- HELP ICON
        help_icon_path = getattr(QStyle, "SP_DialogHelpButton")
        self.help_icon = self.style().standardIcon(help_icon_path)  
        #---------------------------------------------------------------------------------------