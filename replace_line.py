import re

def Fix(fnd,rp,fn):
    NF = ""
    with open(fn, 'r+') as fh:
        text = fh.readlines()
        fix = False
        for i in text:
            print i
            if re.search(r'(?m)^{}'.format(fnd), i):
                i = rp + "## This line has been Fixed!\n"
                fix = True
            NF += i
        if fix:
            print('Found: {}, replacing with: {} '.format(fnd,rp))
        else:
            print("File is fixed, nothing to replace.")
    if fix:
        with open(fn,'w') as File:
            File.write(NF)

def MultiFix(arr,fn):
    for i in arr:
        Fix(arr[0],arr[1],fn)

def main():
    import Example
    import os
    cwd = os.getcwd()
    print "Before fix:\n"
    Example.Xmastree()
    #Because regex is used, some special cases exist. We're looking for an exact match
    #so check https://docs.python.org/3/library/re.html#regular-expression-syntax for syntax
    Fix("    for i in range\(100\):", "    for i in range(50):", "{}/Example.py".format(cwd))
    print("\n After fix:\n")
    reload(Example)
    Example.Xmastree()

if __name__ == "__main__":
    main()
