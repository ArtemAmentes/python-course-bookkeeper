import sys

from PySide6 import QtWidgets
from view.main_view import MainWindow

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())