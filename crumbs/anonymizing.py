import re

import numpy
from art import *
from colorama import Fore, init
from tqdm import tqdm

from crumbs.anonymized_data_conf import fake_map
from crumbs.database_controller import DatabaseBuilder

init(autoreset=True)
query = DatabaseBuilder()


def anonymize_data_basic(db, where_clause, table, keys, values):
    for offset in numpy.arange(0, query.get_count(table), 50000):
        results = select_query(db, keys, offset, table, where_clause)
        if len(results) > 0:
            with tqdm(
                total=(len(results)),
                desc=f"{Fore.CYAN}[{table}]{Fore.RESET}::{Fore.YELLOW}Anonymizing DATA{Fore.RESET}{[i for i in keys[1:]]}{Fore.GREEN}",
            ) as pbar:
                for result in results:
                    list_of_fake_data = []
                    for em, val in enumerate(values[1:]):
                        list_of_fake_data.append(
                            fake_map[val](len(result[em + 1].split()))
                            if result[em + 1] is not None
                            else None
                        )
                    fields_ = (
                        "{}={}".format(
                            first,
                            "'{}'".format(second.replace("'", "''"))
                            if second is not None
                            else "Null",
                        )
                        for first, second in zip(keys[1:], list_of_fake_data)
                    )
                    query.update_query(
                        f"UPDATE {table} SET {', '.join(fields_)} WHERE {keys[0]}={result[0]}"
                    )
                    pbar.update(1)
        else:
            break


def select_query(db, keys, offset, table, where_clause):
    if db == "sqlserver":
        results = query.fetch_all(
            f"SELECT {', '.join([i for i in keys])} "
            f"FROM {table} "
            f"ORDER BY {keys[0]} "
            f"OFFSET {offset} ROWS "
            f"FETCH NEXT 50000 ROWS ONLY"
        )
    if db == "mysql":
        results = query.fetch_all(
            f"SELECT {', '.join([i for i in keys])} "
            f"FROM {table} "
            f"{where_clause} limit 50000 "
            f"offset {offset}"
        )
    return results


def anonymize_json_basic(table, keys, values):
    list_of_fake_keys = []
    for word in re.findall("\w+", str(values)):
        if word.startswith("fake") and word not in list_of_fake_keys:
            list_of_fake_keys.append(word)
    for offset in numpy.arange(0, query.get_count(table), 50000):
        results = query.fetch_all(
            f"SELECT {', '.join([i for i in keys])} "
            f"FROM {table} "
            f"where {keys[1]} is not Null  limit 50000 "
            f"offset {offset}"
        )
        if len(results) > 0:
            with tqdm(
                total=(len(results)),
                desc=f"{Fore.CYAN}[{table}]{Fore.RESET}::{Fore.YELLOW}Anonymizing JSON{Fore.RESET}{[i for i in keys[1:]]}{Fore.GREEN}",
            ) as pbar:
                for result in results:
                    json_template = values[1]
                    for fake in list_of_fake_keys:
                        while fake in json_template:
                            json_template = str(json_template).replace(
                                f"{fake}", fake_map[fake](None), 1
                            )
                    query.update_query(
                        f"UPDATE {table} SET {keys[1]} = '{json_template}' WHERE {keys[0]} = {result[0]}"
                    )
                    pbar.update(1)


def get_keys_and_values(config, table, key):
    keys = list(config[table][key].keys())
    values = list(config[table][key].values())
    return keys, values


def modify(db, tables):
    tprint("Anonymizing Tables", font="cybermedium")
    for table in tables:
        for key in tables[table].keys():
            # get Keys:
            keys, values = get_keys_and_values(tables, table, key)
            if "data" in key:
                where_clause = (
                    f"WHERE {tables[table]['where_clause']}"
                    if "where_clause" in tables[table]
                    else ""
                )
                anonymize_data_basic(db, where_clause, table, keys, values)
                print(f"{Fore.GREEN}Anonymizing {table} complete.\n")
            if "json" in key and db != "sqlserver":
                anonymize_json_basic(table, keys, values)
