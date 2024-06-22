from PySide6.QtWidgets import QVBoxLayout, QWidget
from controllers.main_controller import MainWindow

class MainWidget:
    def __init__(self):
                
        ##########################
        # MAIN WIDGET AND LAYOUT #
        main_widget = QWidget()
        MainWindow.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        #---------------------------------------------------------------------------------------