def setup_preferences_connections(main_window):
    main_window.menuBar.preferencesMenu.zoomIn.triggered.connect(main_window.zoom_in)
    main_window.menuBar.preferencesMenu.zoomOut.triggered.connect(main_window.zoom_out)
    main_window.menuBar.preferencesMenu.darkTheme.triggered.connect(main_window.changeToDarkTheme)
    main_window.menuBar.preferencesMenu.lightTheme.triggered.connect(main_window.changeToLightTheme)
    