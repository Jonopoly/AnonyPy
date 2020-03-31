from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

INTRODUCTION = r"""
 $$$$$$\                                          $$$$$$$\            
$$  __$$\                                         $$  __$$\           
$$ /  $$ |$$$$$$$\   $$$$$$\  $$$$$$$\  $$\   $$\ $$ |  $$ |$$\   $$\ 
$$$$$$$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$$$$$$  |$$ |  $$ |
$$  __$$ |$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |$$  ____/ $$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
$$ |  $$ |$$ |  $$ |\$$$$$$  |$$ |  $$ |\$$$$$$$ |$$ |      \$$$$$$$ |
\__|  \__|\__|  \__| \______/ \__|  \__| \____$$ |\__|       \____$$ |
                                        $$\   $$ |          $$\   $$ |
         - Jon Russell                  \$$$$$$  |          \$$$$$$  |
                                         \______/            \______/ 
"""


def display_database_information(config):
    print(
        f"""
--------------info-------------------
Source: {Fore.GREEN} {config['database']['src']} {Fore.RESET} 
Host: {Fore.GREEN} {config['database']['host']} {Fore.RESET} 
Database: {Fore.GREEN} {config['database']['database']} {Fore.RESET}
User: {Fore.GREEN} {config['database']['user'] if "user" in config['database'] else "N/A"} {Fore.RESET}
Dump Dir: {Fore.GREEN} {config['database']['dump_path'] if "dump_path" in config['database'] else ""} {Fore.RESET}
Start time: {Fore.GREEN} {datetime.now().strftime("%H:%M:%S %p")} {Fore.RESET}
-------------------------------------
    """
    )
