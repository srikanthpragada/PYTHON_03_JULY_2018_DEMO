l = [11, 10, 20, 25, 55]

#
# def iseven(n):
#     return n % 2 == 0


en = filter(lambda n: n % 2 == 0, l)

for n in en:
    print(n)
