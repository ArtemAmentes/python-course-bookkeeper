"""
Модуль содержит код, отвечающий за
запуск приложения.
"""
import PySide6
import sys
from PySide6.QtWidgets import QApplication
from bookkeeper.view.expence_view import MainWindow
from bookkeeper.presenter.expence_presenter import ExpensePresenter
from bookkeeper.presenter.budget_presenter import BudgetPresenter
from bookkeeper.models.category import Category
from bookkeeper.models.expense import Expense
from bookkeeper.repository.sqlite_repository import SQLiteRepository

DB_NAME = 'test.db'

if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = MainWindow()
    model = None

    cat_repo = SQLiteRepository[Category](DB_NAME, Category)
    exp_repo = SQLiteRepository[Expense](DB_NAME, Expense)

    window_expense = ExpensePresenter(model, view, cat_repo, exp_repo)
    window_budget = BudgetPresenter(model, view, exp_repo)
    window_expense.show()
    window_budget.show()
    app.exec_()