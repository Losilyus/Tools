from re import S

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
 
