from PySide6.QtWidgets import QVBoxLayout, QWidget

class MainWidget:
    def __init__(self):
                
        ##########################
        # MAIN WIDGET AND LAYOUT #
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        #---------------------------------------------------------------------------------------