# Expects two arguments - number and limit

import sys

if len(sys.argv) < 3:
    print("Sorry! Invalid number of arguments.")
    sys.exit(1)

num = int(sys.argv[1])
limit = int(sys.argv[2])

for i in range(1, limit + 1):
    print("%2d * %2d = %4d" % (num, i, num * i))
