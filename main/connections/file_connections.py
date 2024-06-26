def setup_file_connections(main_window):
    main_window.menuBar.fileMenu.save.triggered.connect(main_window.save_file)
    main_window.menuBar.fileMenu.saveAs.triggered.connect(main_window.save_file_as)
    main_window.menuBar.fileMenu.open.triggered.connect(main_window.open_file)
    main_window.menuBar.fileMenu.new.triggered.connect(main_window.new_file)
    main_window.menuBar.fileMenu.exit.triggered.connect(main_window.exit_app)
    