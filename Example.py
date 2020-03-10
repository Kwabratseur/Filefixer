def Xmastree():
    str = "*"
    strsp = ""
    for i in range(51):
        strsp += " "
    for i in range(100):
        print(strsp+str)
        str += "**"
        spaces = 50-(i)
        strsp = ""
        for i in range(spaces):
            strsp += " "
