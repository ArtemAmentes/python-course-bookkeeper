import sqlite3

from inspect import get_annotations

from bookkeeper.models.category              import Category
from bookkeeper.models.expense               import Expense
from bookkeeper.models.budget                import Budget
from bookkeeper.repository.sqlite_repository import SQLiteRepository
from bookkeeper.utils                        import read_tree

for db_file in ["database/bookkeeper.db"]:
    for cls in [Category, Expense, Budget]:
        table_name = cls.__name__.lower()
        fields = get_annotations(cls, eval_str=True)
        fields.pop('pk')

        # Create table with name of a class from the list:
        with sqlite3.connect(db_file) as con:
            cur = con.cursor()

            query_fields = ', '.join(fields.keys())
            cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({query_fields})")
        con.close()

cat_repo = SQLiteRepository[Category](db_file="database/bookkeeper.db", cls=Category)

if len(cat_repo.get_all()) == 0:
    cats = '''
    продукты
        мясо
            сырое мясо
            мясные продукты
        сладости
        хлеб
        напитки
            кофе
            чай
            сок
            вода
    развлечения
        кино
        театр
        концерт
        ресторан
    транспорт
        бензин
        метро
        такси
        билеты
            билеты на поезд
            билеты на самолет
            билеты на автобус
    книги
    одежда
    товары для дома
    лекарства
    '''.splitlines()

    Category.create_from_tree(read_tree(cats), cat_repo)