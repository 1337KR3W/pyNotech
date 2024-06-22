from PySide6.QtWidgets import QApplication
from controllers.main_controller import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    notepad = MainWindow()
    notepad.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()