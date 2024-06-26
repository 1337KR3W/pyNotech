def setup_help_connections(main_window):
    main_window.menuBar.helpMenu.about.triggered.connect(main_window.help_about)
    main_window.menuBar.helpMenu.contribute.triggered.connect(main_window.help_contribute)
    main_window.menuBar.helpMenu.moreHelp.triggered.connect(main_window.help_moreHelp)
