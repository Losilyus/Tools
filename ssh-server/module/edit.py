import os
from termcolor import colored, cprint
from tabulate import tabulate
import module.show as show

def editData(hostname, path):

    os.system("clear")

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
        
        os.system("clear")
        print(tabulate(data, headers=["Num", "Hostname", "Host", "User"], tablefmt="fancy_grid"))

        getDetails = input("Edit Host ID> ")
        os.system("clear")

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
            os.system("clear")

            cprint("Press the [Y] key to continue. Press the [N] key to cancel.", "yellow", attrs=["bold"])
            inpContune = input("Continue> ")
            if inpContune == "Y" or inpContune == "y":
                editWrite(f"HostName {data[int(getDetails) - 1][1]}", replace)
                os.system("clear")
                show.show(path)
            show.show(path)
        elif getDetailsOne == "'2'":
            replace = f"User {input('User> ')}"
            os.system("clear")

            cprint("Press the [Y] key to continue. Press the [N] key to cancel.", "yellow", attrs=["bold"])
            inpContune = input("Continue> ")
            if inpContune == "Y" or inpContune == "y":
                editWrite(f"User {data[int(getDetails) - 1][2]}", replace)
                os.system("clear")
                show.show(path)
            show.show(path)
        elif getDetailsOne == "'3'":
            replace = f"Host {input('Host> ')}"
            os.system("clear")

            cprint("Press the [Y] key to continue. Press the [N] key to cancel.", "yellow", attrs=["bold"])
            inpContune = input("Continue> ")
            if inpContune == "Y" or inpContune == "y":
                editWrite(f"Host {data[int(getDetails) - 1][3]}", replace)
                os.system("clear")
                show.show(path)
            show.show(path)
        else:
            err = colored("Err: ", "red", attrs=["bold"])
            cprint(err + "You made a wrong keystroke...", "white", attrs=["bold"])



    elif getDetails == "'n'" or getDetails == "'N'" or getDetails == "'no'" or getDetails == "'NO'":
        os.system("clear")
        show.show(path)
    else:
        try:
            cprint("Successfull...", "green", attrs=["bold"])
        except:
            err = colored("Err: ", "red", attrs=["bold"])
            cprint(err + "You made a wrong keystroke...", "white", attrs=["bold"])