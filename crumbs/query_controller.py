from art import *
from colorama import Fore, init

from crumbs.database_controller import DatabaseBuilder

init(autoreset=True)
sql = DatabaseBuilder()


def truncate_query(tables):
    tprint("Truncating Tables", font="cybermedium")
    for table in tables:
        sql.execute_query_with_disabled_sql_check(f"Truncate {table}")
        print(
            f"{Fore.YELLOW}[TABLE] - {Fore.RESET}{Fore.CYAN}{table}{Fore.RESET} ::{Fore.GREEN} Truncated successfully."
        )


def executable_query(title, queries):
    tprint(title, font="cybermedium")
    for inx, query in enumerate(queries):
        print(
            f'{Fore.GREEN}[{inx + 1}/{len(queries)}]{Fore.RESET} :: "{Fore.YELLOW}{query};{Fore.RESET}" '
        )
        sql.execute_query_with_disabled_sql_check(query)
