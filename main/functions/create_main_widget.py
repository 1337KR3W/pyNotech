from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

def create_main_widget(text_edit):
    main_widget = QWidget()
    main_layout = QVBoxLayout(main_widget)
    hbox_layout = QHBoxLayout()
    hbox_layout.addWidget(text_edit)
    main_layout.addLayout(hbox_layout)
    return main_widget