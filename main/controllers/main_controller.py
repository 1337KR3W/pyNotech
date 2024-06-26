from PySide6.QtWidgets import QMainWindow,QVBoxLayout
from PySide6.QtGui import QFont
from ui.menu_bar.menu_bar import MenuBar
from ui.tool_bar.tool_bar import ToolBar
from ui.bottom_bar.botton_bar import BottomBar
from themes.theme_manager import ThemeManager
from functions.add_widget import add_widget
from functions.new_file import newFile
from functions.save_file import saveFile
from functions.save_file_as import saveFileAs
from functions.open_file import openFile
from functions.check_unsaved_changes import checkUnsaveChanges
from functions.search import searchAndHighlight
from functions.clean_search import cleanSearchTerms
from functions.zoom_in_editor import zoomInEditor
from functions.zoom_out_editor import zoomOutEditor
from functions.show_about import showAbout
from functions.go_git_repo import goGitRepo
from functions.show_more_help import showMoreHelp
from functions.update_window_title import updateWindowTitle
from connections.file_connections import setup_file_connections
from connections.edit_connections import setup_edit_connections
from connections.preferences_connections import setup_preferences_connections
from connections.help_connections import setup_help_connections
from widgets.text_edit import TextEdit
from widgets.main_widget import MainWidget
from configuration.window_settings import WindowSettings

#---------------------------------------------------------------------------------------

#***************************************************************************************
#     _.._   .    .  ._   .   _.._   _____   _.._   _.._  .    .                       *
#    |´    )  \  /  |´ \  |  f    i | `|´ | |´     |´     |    |                       *
#    |___.´    y`   |  |  |  |    |    |    |__    |      |____|                       *
#    |´        |    |  |  |  |    |    |    |´     |      |´  `|                       *
#    i         i    i  L__J   \__/     i    L____  L____  i    i  by josrojrom1        *
#    ¡         :          !     :              ¡          .    :                       *
#              .          :                    .          !                            *
#    .                          .                         .                            *
#                                                                                      *
#                          .                    ¡                                      *
#                                                                                      *
#***************************************************************************************

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #----------------------------------- MAIN WINDOW SETTINGS 
        self.window_settings = WindowSettings()
        self.resize(self.window_settings.resize[0], self.window_settings.resize[1])
        self.initialTitle = self.window_settings.initial_title
        self.setWindowIcon(self.window_settings.pynotech_icon)
        self.setWindowTitle(self.window_settings.initial_title)
        self.current_path = self.window_settings.current_path
        self.current_font_size = self.window_settings.current_font_size
        self.custom_font = self.window_settings.custom_font
        self.recentlyOpen = self.window_settings.recently_open
        #----------------------------------- MAIN WIDGET AND LAYOUT 
        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)
        main_layout = QVBoxLayout(self.main_widget)
        #----------------------------------- TEXT EDITOR 
        self.text_edit = TextEdit(self)
        add_widget(main_layout, self.text_edit)
        #----------------------------------- MENU BAR
        self.menuBar = MenuBar(self)
        self.setMenuBar(self.menuBar)
        #----------------------------------- TOOL BAR
        self.toolBar = ToolBar(self)
        self.addToolBar(self.toolBar)
        #----------------------------------- BOTTOM BAR
        self.bottomBar = BottomBar(self)
        main_layout.addLayout(self.bottomBar)
        #----------------------------------- CONNECTIONS
        setup_file_connections(self)
        setup_edit_connections(self)
        setup_preferences_connections(self)
        setup_help_connections(self)
        #----------------------------------- THEMES 
        self.theme_manager = ThemeManager(
            self,             
            self.menuBar.editMenu,
            self.menuBar.preferencesMenu,
            self.menuBar.helpMenu
        ) 
        # Default Light theme  
        self.theme_manager.set_light_theme()
    #----------------------------------- Dark theme call function            
    def changeToDarkTheme(self):
        self.theme_manager.set_dark_theme()
    #----------------------------------- Light theme call function
    def changeToLightTheme(self):
        self.theme_manager.set_light_theme()
    #----------------------------------- New file call
    def new_file(self):
        newFile(self)
    #----------------------------------- Save file call
    def save_file(self):
        saveFile(self)
    #----------------------------------- Save file as call
    def save_file_as(self):
        saveFileAs(self)
    #----------------------------------- Open file call
    def open_file(self):
        openFile(self)
    #----------------------------------- Exit app call
    def exit_app(self):
        checkUnsaveChanges(self)
    #----------------------------------- Close app call
    # CHECKING "X" BUTTON FROM WINDOW FUNCTION #
    def closeEvent(self, event):
        if self.text_edit.toPlainText():
            self.exit_app()
            event.ignore()
        else:
            self.close
            event.accept()
    #----------------------------------- Copy text call
    def copy_text(self):
        self.text_edit.copy()
    #----------------------------------- Cut text call
    def cut_text(self):
        self.text_edit.cut()
    #----------------------------------- Paste text call
    def paste_text(self):
        self.text_edit.paste()
    #----------------------------------- Select all text call
    def select_all_text(self):
        self.text_edit.selectAll()
    #----------------------------------- Search text call
    def search_and_highlight(self):
        searchAndHighlight(self)
        self.menuBar.editMenu.cleanSearch.setDisabled(False)
        self.toolBar.cleanSearch.setDisabled(False)
    #----------------------------------- Clean text call
    def clean_search_terms(self):
        cleanSearchTerms(self)
    #----------------------------------- Undo text call
    def undo_text(self):
        self.text_edit.undo()
    #----------------------------------- Redo text call
    def redo_text(self):
        self.text_edit.redo()
    #----------------------------------- Redo text call
    def zoom_in(self):
        zoomInEditor(self)
    #----------------------------------- Redo text call
    def zoom_out(self):
        zoomOutEditor(self)
    #----------------------------------- Show about call
    def help_about(self):
        showAbout(self)
    #----------------------------------- Contribute call
    def help_contribute(self):
        goGitRepo(self)
    #----------------------------------- More help call
    def help_moreHelp(self):
        showMoreHelp(self)
    #----------------------------------- Update window title call
    def update_window_title(self):
        updateWindowTitle(self)
    