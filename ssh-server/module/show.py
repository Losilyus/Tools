import scraping as parser

from tabulate import tabulate
import os
from termcolor import colored, cprint
from tabulate import tabulate
import sys

textStart = colored("""
┌────────────────────────────────┐
│       SSH SERVER DETAILS       │
└────────────────────────────────┘
""", "green", attrs=["bold"])

textMenu = colored("""
    E=) Exit
    D=) Details
    T=) Edit
    """, "red", attrs=["bold"])
    

def command(hostname, user): return os.system(f"ssh {user}@{hostname}")


def show(path):

    data = parser.parser(path)

    keyDict = {}
    dataLength = {}

    num = 0

    os.system("cls")
    cprint(textStart, "white", attrs=["bold"])
    for i in data:
        num += 1
        forData = i.split(" ")

        host = forData[0]
        host_name = forData[1]
        user = forData[2]

        keyDict.update(
            {str(f"'{num}'"): {"host": host, "host_name": host_name, "user": user}})
        dataLength.update({str(f"{num}'") : num})

        numberStyle = colored(f"{num}=) ", "yellow", attrs=["bold"])
        userStyle = colored(f"{user}", "green", attrs=["bold"])
        steakStyle = colored(f"{host_name}", "white", attrs=["bold"])


        cprint(numberStyle + steakStyle, "cyan", attrs=["bold"])

    cprint(textMenu, "white", attrs=["bold"])
    tost = "github.com"
   
    get = repr(input("\nSelect Server > "))
    if get == "'e'" or get == "'E'" or get == "'exit'" or get == "'EXIT'":
        sys.exit()
    elif get == "'d'" or get == "'D'":
        os.system("cls")
        # details(keyDict)
    elif get == num: 
        command(keyDict[str(get)]["host_name"], keyDict[str(get)]["user"])
    elif get == "'t'" or get == "'T'":
        os.system("cls")
        #editData(keyDict)
    else:
        try:
            command(keyDict[str(get)]["host_name"], keyDict[str(get)]["user"])
        except:
            err = colored("Err: ", "red", attrs=["bold"])
            cprint(err + "You made a wrong keystroke...", "white", attrs=["bold"])
            os.system("cls")