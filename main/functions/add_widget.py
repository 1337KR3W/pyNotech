from PySide6.QtWidgets import QHBoxLayout

########################
# ADD WIDGETS FUNCTION #
def add_widget(layout, widget):
    hbox = QHBoxLayout()
    hbox.addWidget(widget)
    layout.addLayout(hbox)
#---------------------------------------------------------------------------------------