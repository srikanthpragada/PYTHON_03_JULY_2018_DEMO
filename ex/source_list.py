import os


def print_file(path):
    print("\n ****** ", path, " *********\n")
    file = open(path)
    lineno = 1
    for line in file.readlines():
        print("%3d:%s" % (lineno, line), end='')
        lineno += 1


files = os.walk(r"e:\classroom\python\july3")

for (dn, dl, fl) in files:
    if dn.find('.git') >= 0:  # ignore GIT folder
        continue

    for file in fl:
        if file.endswith(".py"):
            print_file(dn + "\\" + file)
