import sqlite3
from database.queries import Queries


class DataBase:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(Queries.saving_survey_results)
            conn.execute(Queries.create_table_categories)
            conn.execute(Queries.create_table_dishes)
            conn.execute(Queries.insert_into_categories)
            conn.execute(Queries.insert_into_dishes)
            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)

    def fetch(self, query: str, params: tuple = None, fetchall: bool = True):
        with sqlite3.connect(self.path) as conn:
            result = conn.execute(query, params)
            return result.fetchall()
