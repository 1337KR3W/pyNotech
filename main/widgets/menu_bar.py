from PySide6.QtWidgets import QWidgetAction, QToolBar
from PySide6.QtGui import QIcon
from icons.icons import Icons

class MenuBar:
    def __init__(self):

        ###################################
        # DEFAULT MENU BAR OF QMainWindow #
        menuBar = self.menuBar()
        # ---------#
        # TOOL BAR #
        toolBar = QToolBar()
        toolBar.setMovable(False)
        self.addToolBar(toolBar)
        #---- TOOL BAR ACTIONS
        #------------------------- NEW ACTION
        self.new = QWidgetAction(self)  
        self.new.setIcon(Icons.new_icon)
        self.new.setShortcut("Ctrl+N")
        self.new.setIconText("New")
        #------------------------- OPEN ACTION
        self.open = QWidgetAction(self)
        self.open.setIcon(Icons.open_icon)
        self.open.setShortcut("Ctrl+O")
        self.open.setIconText("Open")
        #------------------------- SAVE ACTION
        self.save = QWidgetAction(self)
        self.save.setIcon(Icons.save_icon)
        self.save.setShortcut("Ctrl+S")
        self.save.setIconText("Save")
        #------------------------- SAVE AS ACTION
        self.saveAs = QWidgetAction(self)
        self.saveAs.setIcon(Icons.save_icon)
        self.saveAs.setShortcut("Ctrl+Shift+S")
        self.saveAs.setIconText("Save as...")
        #------------------------- EXIT ACTION
        self.exit = QWidgetAction(self)
        self.exit.setIcon(Icons.exit_icon)
        self.exit.setShortcut("Ctrl+Q")
        self.exit.setIconText("Exit")
        #------------------------- COPY ACTION
        self.copy = QWidgetAction(self)  
        self.copy.setIcon(QIcon("../../resources/icons/copy_icon.PNG"))
        self.copy.setShortcut("Ctrl+C")
        self.copy.setIconText("Copy")
        #------------------------- CUT ACTION
        self.cut = QWidgetAction(self)
        self.cut.setIcon(QIcon("../../resources/icons/cut_icon.PNG"))
        self.cut.setShortcut("Ctrl+X")
        self.cut.setIconText("Cut")
        #------------------------- PASTE ACTION
        self.paste = QWidgetAction(self)
        self.paste.setIcon(QIcon("../../resources/icons/paste_icon.PNG"))
        self.paste.setShortcut("Ctrl+V")
        self.paste.setIconText("Paste")
        #------------------------- SELECT ALL ACTION
        self.selectAll = QWidgetAction(self)
        self.selectAll.setIcon(Icons.selectAll_icon)
        self.selectAll.setShortcut("Ctrl+A")
        self.selectAll.setIconText("Select all")
        #------------------------- SEARCH ACTION
        self.search = QWidgetAction(self)
        self.search.setIcon(Icons.search_icon)
        self.search.setShortcut("Ctrl+F")
        self.search.setIconText("Search")
        #------------------------- CLEAN SEARCH ACTION
        self.cleanSearch = QWidgetAction(self)
        self.cleanSearch.setIcon(Icons.cleanSearch_icon)
        self.cleanSearch.setShortcut("Ctrl+B")
        self.cleanSearch.setIconText("Clean search")
        self.cleanSearch.setDisabled(True)
        #------------------------- UNDO ACTION
        self.undo = QWidgetAction(self)
        self.undo.setIcon(self.undo_icon)
        self.undo.setShortcut("Ctrl+Z")
        self.undo.setIconText("Undo")
        #------------------------- REDO ACTION
        self.redo = QWidgetAction(self)
        self.redo.setIcon(self.redo_icon)
        self.redo.setShortcut("Ctrl+Y")
        self.redo.setIconText("Redo")
        #------------------------- ZOOM IN ACTION
        self.zoomIn = QWidgetAction(self)
        self.zoomIn.setIcon(QIcon("../../resources/icons/zoomIn_icon.PNG"))
        self.zoomIn.setShortcut("Ctrl++")
        self.zoomIn.setIconText("Zoom In")
        #------------------------- ZOOM OUT ACTION
        self.zoomOut = QWidgetAction(self)
        self.zoomOut.setIcon(QIcon("../../resources/icons/zoomOut_icon.PNG"))
        self.zoomOut.setShortcut("Ctrl+-")
        self.zoomOut.setIconText("Zoom Out")
        #------------------------- APPEARANCE SELECT ACTION
        self.appearance = QWidgetAction(self)
        self.appearance.setIconText("Appearance")
        #------------------------- DARK THEME 
        self.darkTheme = QWidgetAction(self)
        self.darkTheme.setIconText("Dark mode")
        #------------------------- LIGHT THEME
        self.lightTheme = QWidgetAction(self)
        self.lightTheme.setIconText("Light mode")
        #------------------------- ABOUT ACTION
        self.about = QWidgetAction(self)
        self.about.setIcon(self.about_icon)
        self.about.setIconText("About")
        #------------------------- CONTRIBUTE ACTION
        self.contribute = QWidgetAction(self)
        self.contribute.setIcon(QIcon("../../resources/icons/github-mark.PNG"))
        self.contribute.setIconText("Contribute")
        #------------------------- MORE HELP ACTION
        self.moreHelp = QWidgetAction(self)
        self.moreHelp.setIcon(Icons.help_icon)
        self.moreHelp.setIconText("More help...")
        #---------------------------------------------------------------------------------------
        #---- TOOL BAR ADDED ACTIONS
        toolBar.addAction(self.new)
        toolBar.addAction(self.open)
        toolBar.addAction(self.save)
        toolBar.addSeparator()
        toolBar.addAction(self.search)
        toolBar.addAction(self.cleanSearch)
        #---- FILE MENU BAR OPTIONS  
        fileMenu = menuBar.addMenu('File')
        fileMenu.addAction(self.new)
        fileMenu.addAction(self.open)
        fileMenu.addAction(self.save)
        fileMenu.addAction(self.saveAs)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exit)
        #---- EDIT MENU BAR OPTIONS  
        editMenu = menuBar.addMenu('Edit')
        editMenu.addAction(self.copy)
        editMenu.addAction(self.cut)
        editMenu.addAction(self.paste)
        editMenu.addSeparator()
        editMenu.addAction(self.selectAll)
        editMenu.addAction(self.search)
        editMenu.addSeparator()
        editMenu.addAction(self.undo)
        editMenu.addAction(self.redo)
        #---- PREFERENCES MENU BAR OPTIONS  
        preferencesMenu = menuBar.addMenu('Preferences')
        preferencesMenu.addAction(self.zoomIn)
        preferencesMenu.addAction(self.zoomOut)
        #--------------- APPEARANCE SELECT OPTION
        self.appearance = preferencesMenu.addMenu('Appearance')
        self.appearance.setIcon(self.appearance_icon)
        self.appearance.addAction(self.darkTheme)
        self.appearance.addAction(self.lightTheme)
        #---- HELP MENU BAR OPTIONS  
        helpMenu = menuBar.addMenu('Help')
        helpMenu.addAction(self.about)
        helpMenu.addAction(self.contribute)
        helpMenu.addAction(self.moreHelp)
        #---------------------------------------------------------------------------------------