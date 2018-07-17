import sys

# print(sys.argv)

num = int(sys.argv[1])

fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial of %d is %d" % (num, fact))
