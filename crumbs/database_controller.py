import json

import mysql.connector


class DatabaseBuilder:
    def __init__(self):
        with open(r"config/settings.json", "r") as file:
            configuration = json.load(file)

        my_sql_config = {
            "user": configuration["database"]["user"],
            "password": configuration["database"]["password"],
            "host": configuration["database"]["host"],
            "database": configuration["database"]["database"],
            "raise_on_warnings": True,
        }
        self.cnx = mysql.connector.connect(**my_sql_config)
        self.cursor = self.cnx.cursor()
        self.cursor2 = self.cnx.cursor(buffered=True)

    def fetch_all(self, query):
        self.cursor.execute(query)
        results = []
        for row in self.cursor:
            results.append(row)
        return results

    def update_query(self, query):
        self.cursor2.execute(query)
        self.cnx.commit()

    def get_count(self, table):
        self.cursor2.execute(f"SELECT COUNT(*) from {table}")
        return self.cursor2.fetchone()[0]

    def execute_query_with_disabled_sql_check(self, table: str):
        query = f"SET FOREIGN_KEY_CHECKS=0; {str(table)}; SET FOREIGN_KEY_CHECKS=1;"
        for cur in self.cursor2.execute(query, multi=True):
            cur
            if cur.with_rows:
                cur.fetchall()
        self.cnx.commit()
