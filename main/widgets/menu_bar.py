from PySide6.QtWidgets import QWidgetAction, QToolBar, QMenuBar
from PySide6.QtGui import QIcon
from icons.icons import *

def create_menu_bar(parent):

    ###################################
    # DEFAULT MENU BAR OF QMainWindow #
    menuBar = QMenuBar(parent)
    # ---------#
    # TOOL BAR #
    toolBar = QToolBar()
    toolBar.setMovable(False)
    #---- TOOL BAR ACTIONS
    #------------------------- NEW ACTION
    new = QWidgetAction()  
    new.setIcon(new_icon)
    new.setShortcut("Ctrl+N")
    new.setIconText("New")
    #------------------------- OPEN ACTION
    open = QWidgetAction()
    open.setIcon(open_icon)
    open.setShortcut("Ctrl+O")
    open.setIconText("Open")
    #------------------------- SAVE ACTION
    save = QWidgetAction()
    save.setIcon(save_icon)
    save.setShortcut("Ctrl+S")
    save.setIconText("Save")
    #------------------------- SAVE AS ACTION
    saveAs = QWidgetAction()
    saveAs.setIcon(save_icon)
    saveAs.setShortcut("Ctrl+Shift+S")
    saveAs.setIconText("Save as...")
    #------------------------- EXIT ACTION
    exit = QWidgetAction()
    exit.setIcon(exit_icon)
    exit.setShortcut("Ctrl+Q")
    exit.setIconText("Exit")
    #------------------------- COPY ACTION
    copy = QWidgetAction()  
    copy.setIcon(QIcon("../../resources/icons/copy_icon.PNG"))
    copy.setShortcut("Ctrl+C")
    copy.setIconText("Copy")
    #------------------------- CUT ACTION
    cut = QWidgetAction()
    cut.setIcon(QIcon("../../resources/icons/cut_icon.PNG"))
    cut.setShortcut("Ctrl+X")
    cut.setIconText("Cut")
    #------------------------- PASTE ACTION
    paste = QWidgetAction()
    paste.setIcon(QIcon("../../resources/icons/paste_icon.PNG"))
    paste.setShortcut("Ctrl+V")
    paste.setIconText("Paste")
    #------------------------- SELECT ALL ACTION
    selectAll = QWidgetAction()
    selectAll.setIcon(selectAll_icon)
    selectAll.setShortcut("Ctrl+A")
    selectAll.setIconText("Select all")
    #------------------------- SEARCH ACTION
    search = QWidgetAction()
    search.setIcon(search_icon)
    search.setShortcut("Ctrl+F")
    search.setIconText("Search")
    #------------------------- CLEAN SEARCH ACTION
    cleanSearch = QWidgetAction()
    cleanSearch.setIcon(cleanSearch_icon)
    cleanSearch.setShortcut("Ctrl+B")
    cleanSearch.setIconText("Clean search")
    cleanSearch.setDisabled(True)
    #------------------------- UNDO ACTION
    undo = QWidgetAction()
    undo.setIcon(undo_icon)
    undo.setShortcut("Ctrl+Z")
    undo.setIconText("Undo")
    #------------------------- REDO ACTION
    redo = QWidgetAction()
    redo.setIcon(redo_icon)
    redo.setShortcut("Ctrl+Y")
    redo.setIconText("Redo")
    #------------------------- ZOOM IN ACTION
    zoomIn = QWidgetAction()
    zoomIn.setIcon(QIcon("../../resources/icons/zoomIn_icon.PNG"))
    zoomIn.setShortcut("Ctrl++")
    zoomIn.setIconText("Zoom In")
    #------------------------- ZOOM OUT ACTION
    zoomOut = QWidgetAction()
    zoomOut.setIcon(QIcon("../../resources/icons/zoomOut_icon.PNG"))
    zoomOut.setShortcut("Ctrl+-")
    zoomOut.setIconText("Zoom Out")
    #------------------------- APPEARANCE SELECT ACTION
    appearance = QWidgetAction()
    appearance.setIconText("Appearance")
    #------------------------- DARK THEME 
    darkTheme = QWidgetAction()
    darkTheme.setIconText("Dark mode")
    #------------------------- LIGHT THEME
    lightTheme = QWidgetAction()
    lightTheme.setIconText("Light mode")
    #------------------------- ABOUT ACTION
    about = QWidgetAction()
    about.setIcon(about_icon)
    about.setIconText("About")
    #------------------------- CONTRIBUTE ACTION
    contribute = QWidgetAction()
    contribute.setIcon(QIcon("../../resources/icons/github-mark.PNG"))
    contribute.setIconText("Contribute")
    #------------------------- MORE HELP ACTION
    moreHelp = QWidgetAction()
    moreHelp.setIcon(help_icon)
    moreHelp.setIconText("More help...")
    #---------------------------------------------------------------------------------------
    #---- TOOL BAR ADDED ACTIONS
    toolBar.addAction(new)
    toolBar.addAction(open)
    toolBar.addAction(save)
    toolBar.addSeparator()
    toolBar.addAction(search)
    toolBar.addAction(cleanSearch)
    #---- FILE MENU BAR OPTIONS  
    fileMenu = menuBar.addMenu('File')
    fileMenu.addAction(new)
    fileMenu.addAction(open)
    fileMenu.addAction(save)
    fileMenu.addAction(saveAs)
    fileMenu.addSeparator()
    fileMenu.addAction(exit)
    #---- EDIT MENU BAR OPTIONS  
    editMenu = menuBar.addMenu('Edit')
    editMenu.addAction(copy)
    editMenu.addAction(cut)
    editMenu.addAction(paste)
    editMenu.addSeparator()
    editMenu.addAction(selectAll)
    editMenu.addAction(search)
    editMenu.addSeparator()
    editMenu.addAction(undo)
    editMenu.addAction(redo)
    #---- PREFERENCES MENU BAR OPTIONS  
    preferencesMenu = menuBar.addMenu('Preferences')
    preferencesMenu.addAction(zoomIn)
    preferencesMenu.addAction(zoomOut)
    #--------------- APPEARANCE SELECT OPTION
    appearance = preferencesMenu.addMenu('Appearance')
    appearance.setIcon(appearance_icon)
    appearance.addAction(darkTheme)
    appearance.addAction(lightTheme)
    #---- HELP MENU BAR OPTIONS  
    helpMenu = menuBar.addMenu('Help')
    helpMenu.addAction(about)
    helpMenu.addAction(contribute)
    helpMenu.addAction(moreHelp)
    #---------------------------------------------------------------------------------------