from PySide6.QtGui import QIcon
from icons.icons import Icons
import os

########################
# LIGHT THEME FUNCTION #
def setLightTheme(self):
    icons = Icons()
    undo_icon = icons.undo_icon()
    redo_icon = icons.redo_icon()
    main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    lightThemeStyle = '''
    QWidget{background-color: rgb(255,255,255);color: #000000;}
    QTextEdit{background-color: rgb(245,245,245);}
    QMenu::item:selected{background-color: rgb(210,210,210);}
    '''
    self.setStyleSheet(lightThemeStyle)
    self.zoomIn.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'zoomIn_icon.PNG')))
    self.zoomOut.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'zoomOut_icon.PNG')))
    self.copy.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'copy_icon.PNG')))
    self.cut.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'cut_icon.PNG')))
    self.paste.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'paste_icon.PNG')))
    self.contribute.setIcon(QIcon(os.path.join(main_dir, 'resources', 'icons', 'github-mark.PNG')))
    self.undo.setIcon(undo_icon)
    self.redo.setIcon(redo_icon)
#---------------------------------------------------------------------------------------