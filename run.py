#! /usr/bin/env python
## Coronavirus-Stats v1.0 (Requires Python3.6 or Higher)
## Author: AgentNumber47
## Source: https://github.com/Agentnumber47/Coronavirus-Stats
## Wear a mask!

from colorama import init
from covid import Covid
from datetime import datetime
import os
import platform

def place_value(number):
    return ("{:,}".format(number))

def main():
    init()

    # Detect OS (to define clear screen code)
    operating_system = platform.system()
    clear_command = "cls" if operating_system == "Windows" else "clear"
    # Detect terminal size for display purposes
    terminal_size = os.get_terminal_size()
    columns = terminal_size.columns

    # Capture time
    time_of_now = datetime.now()
    querytime = f"{time_of_now.day} {time_of_now.strftime('%b')} {time_of_now.year} [{time_of_now.hour}:{time_of_now.minute}:{time_of_now.second}]"

    # Load coronavirus data
    covid = Covid(source="worldometers")
    usa_cases = covid.get_status_by_country_name('usa')
    world_cases = {}
    world_cases['confirmed'] = place_value(covid.get_total_confirmed_cases())
    world_cases['deaths'] = place_value(covid.get_total_deaths())
    world_cases['active'] = place_value(covid.get_total_active_cases())
    world_cases['recovered'] = place_value(covid.get_total_recovered())

    # Manage the data for printing to shell
    color_map = {'confirmed': 35, 'deaths': 31, 'active': 33, 'recovered': 32} # Set the Colorama color codes for stats
    stat_list = ['confirmed', 'deaths', 'active', 'recovered']

    # Print data to shell
    os.system(clear_command)
    print('\033[36m' + "#".center(columns, "#"))
    print("     US | GLOBAL COVID STATISTICS     ".center(columns, "#"))
    print("#".center(columns, "#"))
    print("")
    for i in stat_list:
        print(f'\033[{color_map[i]}m' + f"{i.upper()}".center(columns, " "))
        print(f"{place_value(usa_cases[i])} | {world_cases[i]}".center(columns, " "))
        print("")
    print('\033[39m') # Reset text color
    print(f"Source: Worldometers ({querytime})".rjust(columns, " "))
    pause = input("")


if __name__ == '__main__':
    main()
