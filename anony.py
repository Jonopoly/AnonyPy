from json import load
from time import time, sleep
from colorama import Fore, init

from crumbs.Introduction import INTRODUCTION, display_database_information
from crumbs.query_controller import truncate_query, executable_query
from crumbs.anonymizing import modify


init(autoreset=True)

start_time = time()


with open(r"config/settings.json", "r") as f:
    configuration = load(f)
    RDB = configuration["database"]["src"]

print(INTRODUCTION)
display_database_information(configuration)
sleep(2)

list_of_functions = [
    lambda: truncate_query(RDB, configuration["truncate"]), #Works!
    lambda: executable_query(RDB, "Custom Queries", configuration["custom_queries"]),
    lambda: modify(RDB, configuration["table_data"]),
    lambda: executable_query(RDB, "Final Queries", configuration["final_queries"]),
]
#
for function in list_of_functions:
    try:
        function()
    except KeyError as e:
        print(f"{Fore.YELLOW}[WARN] {Fore.RESET}{e} not declared.")
#
print(f"Finished! Completion Time:  ({round(time() - start_time, 2)} seconds)")
