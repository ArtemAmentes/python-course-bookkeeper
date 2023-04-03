"""
MainWindow view
"""

from PySide6 import QtWidgets
from PySide6.QtWidgets import (QWidget)

from .expense_vid import ExpenceWidget
from .budget_vid import BudgetWidget
from .edit import EditWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Bookkeeper")

        layout = QtWidgets.QVBoxLayout()
        expence = ExpenceWidget()
        budget = BudgetWidget()
        edit_field = EditWidget()

        layout.addWidget(expence)
        layout.addWidget(budget)
        layout.addWidget(edit_field)

        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)