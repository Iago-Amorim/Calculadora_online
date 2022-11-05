import sys

from PyQt6.QtWidgets  import QMainWindow, QApplication
from Calculadora import Ui_Calculadora

class MainWindow(QMainWindow, Ui_Calculadora):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    qt.exec()