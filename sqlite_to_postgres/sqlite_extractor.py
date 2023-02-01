import sqlite3


class SQLiteExtractor:
    def __init__(self, conn):
        self.conn = conn
        self.curs = self.conn.cursor()

    def get_cursor_from_sqlite(self, table: str) -> sqlite3.Connection.cursor:
        """Выбор всех данных из заблицы и возвращение курсора."""
        self.curs.execute(f"SELECT * FROM {table};")
        return self.curs

    def get_batch_from_sqlite(self) -> tuple:
        """Получение части записей из SQLite."""
        return self.curs.fetchmany(5000)
