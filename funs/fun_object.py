def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


def mathop(n1, n2, task):
    return task(n1, n2)


print(mathop(10, 20, add))
print(mathop(10, 20, mul))




