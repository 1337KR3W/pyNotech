from PySide6.QtGui import QIcon
import os
from icons.icons import *

#######################
# DARK THEME FUNCTION #
def setDarkTheme(self):
    icons = Icons()
    undo_icon_w = icons.undo_icon_w()
    redo_icon_w = icons.redo_icon_w()
    main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    darkThemeStyle = '''
    QWidget{background-color: rgb(49,49,49);color: #FFFFFF;}
    QTextEdit{background-color: rgb(29,29,29);}
    QMenuBar::item:selected{color: #000000;}
    QMenu::item:selected{background-color: rgb(66,66,66);}
    '''
    self.setStyleSheet(darkThemeStyle)
    self.zoomIn.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'zoomIn_icon_w.PNG')))
    self.zoomOut.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'zoomOut_icon_w.PNG')))
    self.copy.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'copy_icon_w.PNG')))
    self.cut.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'cut_icon_w.PNG')))
    self.paste.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'paste_icon_w.PNG')))
    self.contribute.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'github-mark-white.PNG')))
    self.undo.setIcon(undo_icon_w)
    self.redo.setIcon(redo_icon_w)
#---------------------------------------------------------------------------------------