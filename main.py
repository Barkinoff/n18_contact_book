from ui import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    exit(app.exec())