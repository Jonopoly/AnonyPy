import json

import mysql.connector
import pyodbc
import psycopg2


class DatabaseBuilder:
    def __init__(self):
        with open(r"config/settings.json", "r") as file:
            configuration = json.load(file)

        if configuration["database"]["src"] == "postgresql":
            self.cnx = psycopg2.connect(
                host=configuration['database']['host'],
                database=configuration['database']['database'],
                user=configuration['database']['user'],
                password=configuration['database']['password']
            )
            self.cursor = self.cnx.cursor()

        if configuration["database"]["src"] == "sqlserver":
            self.cnx = pyodbc.connect(
                "Driver={SQL Server};"
                f'Server={configuration["database"]["host"]};'
                f'Database={configuration["database"]["database"]};'
                "Trusted_Connection=yes;"
            )
            self.cursor = self.cnx.cursor()

        if configuration["database"]["src"] == "mysql":
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
        self.cursor.execute(query)
        self.cnx.commit()

    def get_count(self, table):
        self.cursor.execute(f"SELECT COUNT(*) from {table}")
        return self.cursor.fetchone()[0]

    def execute_query_with_disabled_sql_check(self, table: str):
        query = f"SET FOREIGN_KEY_CHECKS=0; {str(table)}; SET FOREIGN_KEY_CHECKS=1;"
        for cur in self.cursor2.execute(query, multi=True):
            cur
            if cur.with_rows:
                cur.fetchall()
        self.cnx.commit()

    def sqlServerTruncateQuery(self, table: str):
        self.cursor.execute(str(table))
        self.cnx.commit()
        pass
