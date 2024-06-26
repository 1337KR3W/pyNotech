
def setup_edit_connections(main_window):
    main_window.menuBar.editMenu.copy.triggered.connect(main_window.copy_text)
    main_window.menuBar.editMenu.paste.triggered.connect(main_window.paste_text)
    main_window.menuBar.editMenu.cut.triggered.connect(main_window.cut_text)
    #main_window.menuBar.editMenu.search.triggered.connect(main_window.searchAndHighlight)
    #main_window.menuBar.editMenu.cleanSearch.triggered.connect(main_window.cleanSearchTerms)
    #main_window.menuBar.editMenu.undo.triggered.connect(main_window.undo)
    #main_window.menuBar.editMenu.redo.triggered.connect(main_window.redo)