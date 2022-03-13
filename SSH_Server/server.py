from dataclasses import replace
from email import charset
from email.mime import base
import os
from re import S
import sys
from tabulate import tabulate
from termcolor import colored, cprint

# textStart = colored("""
# ┌───────────────────────────────────┐  
# │        SSH SERVER DETAILS         │
# │                                   │
# ├───────────────────────────────────┤
# │ E │EXIT    │  Exits The Program.  │
# ├───┼────────┼──────────────────────┤
# │ D │DETAILS │  Details The Program.│
# ├───┼────────┼──────────────────────┤
# │ T │Edit    │  Edit The Program.   │
# └───┴────────┴──────────────────────┘
#     """, "green", attrs=["bold"]) 

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



def parser(path):
    all = ""
    lines = []
    with open(path, "r") as f:
        for i in f.readlines():
            lines.append(i)
        f.close()

    num = 0
    info = ""
    allInfo = []
    for i in lines:
        if num == 3:
            all += str(info)
            allInfo.append(info)
            num = 0
            info = ""
        else:
            if "Host " in i:
                num += 1
                info += i.replace("Host ", "").replace("\n",
                                                       "").replace(" ", "") + " "
            elif "HostName" in i:
                num += 1
                info += i.replace("HostName ", "").replace("\n",
                                                           "").replace(" ", "") + " "
            elif "User " in i:
                num += 1
                info += i.replace("User ", "").replace("\n",
                                                       "").replace(" ", "")
    return allInfo
    
def command(hostname, user): return os.system(f"ssh {user}@{hostname}")


def editData(hostname):

    os.system("cls")

    data = []
    lengthTable = 0

    for var in hostname:
        lengthTable += 1
        data.append([lengthTable, hostname[var]["host_name"], hostname[var]["user"], hostname[var]["host"]])

    cprint("""
q=) Quit
e=) Edit
    """, "yellow", attrs=["bold"])
    def editWrite (search, replace):
        search = search
        replace = replace
        with open(path, "r") as f:
            data = f.read()
            data = data.replace(search, replace)
        with open(path, "w") as f:
            f.write(data)
            
    
    getDetails = repr(input("> "))
    
    if getDetails == "'e'" or getDetails == "'E'":
        
        os.system("cls")
        print(tabulate(data, headers=["Num", "Hostname", "Host", "User"], tablefmt="fancy_grid"))

        getDetails = input("Edit Host ID> ")
        os.system("cls")

        hostnameText = colored(f"1=) Hostname ", "white", attrs=["bold"])
        hostnameTextData = colored(data[int(getDetails) - 1][1], "white", attrs=["bold"])
        userText = colored(f"2=) User: ", "white", attrs=["bold"])
        userTextData = colored(data[int(getDetails) - 1][2], "white", attrs=["bold"])
        hostText = colored(f"3=) Host: ", "white", attrs=["bold"])
        hostTextData = colored(data[int(getDetails) - 1][3], "white", attrs=["bold"])
        menuText = hostnameText+hostnameTextData+"\n"+userText+userTextData+"\n"+hostText+hostTextData
        cprint(menuText, "white", attrs=["bold"])
        
        cprint("\nPlease select the type you want to edit.", "yellow", attrs=["bold"])
        getDetailsOne = repr(input("Data> "))

        if getDetailsOne == "'1'":
            replace = f"HostName {input('Hostname> ')}"
            os.system("cls")

            cprint("Press the [Y] key to continue. Press the [N] key to cancel.", "yellow", attrs=["bold"])
            inpContune = input("Continue> ")
            if inpContune == "Y" or inpContune == "y":
                editWrite(f"HostName {data[int(getDetails) - 1][1]}", replace)
                os.system("cls")
                show(path)
            show(path)
        elif getDetailsOne == "'2'":
            replace = f"User {input('User> ')}"
            os.system("cls")

            cprint("Press the [Y] key to continue. Press the [N] key to cancel.", "yellow", attrs=["bold"])
            inpContune = input("Continue> ")
            if inpContune == "Y" or inpContune == "y":
                editWrite(f"User {data[int(getDetails) - 1][2]}", replace)
                os.system("cls")
                show(path)
            show(path)
        elif getDetailsOne == "'3'":
            replace = f"Host {input('Host> ')}"
            os.system("cls")

            cprint("Press the [Y] key to continue. Press the [N] key to cancel.", "yellow", attrs=["bold"])
            inpContune = input("Continue> ")
            if inpContune == "Y" or inpContune == "y":
                editWrite(f"Host {data[int(getDetails) - 1][3]}", replace)
                os.system("cls")
                show(path)
            show(path)
        else:
            err = colored("Err: ", "red", attrs=["bold"])
            cprint(err + "You made a wrong keystroke...", "white", attrs=["bold"])



    elif getDetails == "'n'" or getDetails == "'N'" or getDetails == "'no'" or getDetails == "'NO'":
        os.system("cls")
        show(path)
    else:
        try:
            print("sfas")


           
            cprint("Successfull...", "green", attrs=["bold"])
        except:
            err = colored("Err: ", "red", attrs=["bold"])
            cprint(err + "You made a wrong keystroke...", "white", attrs=["bold"])



def details(hostname):

    os.system("cls")

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
        show(path)
    else:
        err = colored("Err: ", "red", attrs=["bold"])
        cprint(err + "You made a wrong keystroke...", "white", attrs=["bold"])

def show(path):

    data = parser(path)

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
        details(keyDict)
    elif get == num: 
        command(keyDict[str(get)]["host_name"], keyDict[str(get)]["user"])
    elif get == "'t'" or get == "'T'":
        os.system("cls")
        editData(keyDict)
    else:
        try:
            command(keyDict[str(get)]["host_name"], keyDict[str(get)]["user"])
        except:
            err = colored("Err: ", "red", attrs=["bold"])
            cprint(err + "You made a wrong keystroke...", "white", attrs=["bold"])
            os.system("cls")

path = r"C:\Users\fahre\.ssh\configs"

show(path)