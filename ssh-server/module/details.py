import os
from termcolor import colored, cprint
from tabulate import tabulate
import sys

import module.show as show

textMenu = colored("""
    E=) Exit
    D=) Details
    T=) Edit
    """, "red", attrs=["bold"])
    

def details(hostname, path):
    os.system("clear")

    data = []
    lengthTable = 0

    for var in hostname:
        lengthTable += 1
        data.append([lengthTable, hostname[var]["host_name"], hostname[var]["user"], hostname[var]["host"]])

    print(tabulate(data, headers=["Num", "Hostname", "User", "Host"], tablefmt="fancy_grid"))

    print(textMenu)
    getDetails = repr(input("\nSelect > "))
    if getDetails == "'e'" or getDetails == "'E'" or getDetails == "'exit'" or getDetails == "'EXIT'":
        sys.exit()
    elif getDetails == "'q'" or getDetails == "'Q'":
        os.system("cls")
        show.show(path)
    else:
        err = colored("Err: ", "red", attrs=["bold"])
        show.cprint(err + "You made a wrong keystroke...", "white", attrs=["bold"])