from icons.icons import Icons

class ThemeManager:
    def __init__(self, main_window, edit_menu, preferences_menu, help_menu):
        self.main_window = main_window
        self.edit_menu = edit_menu
        self.preferences_menu = preferences_menu
        self.help_menu = help_menu
        self.icons = Icons()
    #----------------------------------- LIGHT THEME
    def set_light_theme(self):
        light_theme_style = '''
        QWidget{background-color: rgb(255,255,255);color: #000000;}
        QTextEdit{background-color: rgb(245,245,245);}
        QMenu::item:selected{background-color: rgb(210,210,210);}
        '''
        copy_icon = self.icons.copy_icon()
        cut_icon = self.icons.cut_icon()
        paste_icon = self.icons.paste_icon()
        undo_icon = self.icons.undo_icon()
        redo_icon = self.icons.redo_icon()
        zoomIn_icon = self.icons.zoomIn_icon()
        zoomOut_icon = self.icons.zoomOut_icon()
        contribute_icon = self.icons.contribute_icon()
        self.main_window.setStyleSheet(light_theme_style)
        self.edit_menu.copy.setIcon(copy_icon)
        self.edit_menu.cut.setIcon(cut_icon)
        self.edit_menu.paste.setIcon(paste_icon)
        self.edit_menu.undo.setIcon(undo_icon)
        self.edit_menu.redo.setIcon(redo_icon)
        self.preferences_menu.zoomIn.setIcon(zoomIn_icon)
        self.preferences_menu.zoomOut.setIcon(zoomOut_icon)
        self.help_menu.contribute.setIcon(contribute_icon)
    #----------------------------------- DARK THEME
    def set_dark_theme(self):
        dark_theme_style = '''
        QWidget{background-color: rgb(53,53,53);color: rgb(255,255,255);}
        QTextEdit{background-color: rgb(70,70,70);}
        QMenuBar::item:selected{color: #000000;}
        QMenu::item:selected{background-color: rgb(66,66,66);}
        '''
        undo_icon = self.icons.undo_icon_w()
        redo_icon = self.icons.redo_icon_w()
        copy_icon = self.icons.copy_icon_w()
        cut_icon = self.icons.cut_icon_w()
        paste_icon = self.icons.paste_icon_w()
        zoomIn_icon = self.icons.zoomIn_icon_w()
        zoomOut_icon = self.icons.zoomOut_icon_w()
        contribute_icon = self.icons.contribute_icon_w()
        self.main_window.setStyleSheet(dark_theme_style)
        self.edit_menu.copy.setIcon(copy_icon)
        self.edit_menu.cut.setIcon(cut_icon)
        self.edit_menu.paste.setIcon(paste_icon)
        self.edit_menu.undo.setIcon(undo_icon)
        self.edit_menu.redo.setIcon(redo_icon)
        self.preferences_menu.zoomIn.setIcon(zoomIn_icon)
        self.preferences_menu.zoomOut.setIcon(zoomOut_icon)
        self.help_menu.contribute.setIcon(contribute_icon)