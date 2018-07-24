
def even_nums(n):
    for i in range(2,n+1,2):
        yield i


print(even_nums(10))

for n in even_nums(10):
    print(n)