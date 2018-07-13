def add(n1, n2):
    return n1 + n2


def print_nums(start=1, end=10):
    for i in range(start, end):
        print(i, end=' ')
    else:
        print()


def total_nums(*nums):
    total = 0
    for n in nums:
        total += n

    return total


print(total_nums(10, 20, 30))

print(add(10, 20))
print(add('a', 'b'))
# print(add('a', 10))  # error

print_nums(5)
print_nums(5, 20)
print_nums(end=5, start=2)
