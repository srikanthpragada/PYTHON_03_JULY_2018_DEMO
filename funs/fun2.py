def greet(msg, *names):
    for n in names:
        print(msg, n)


def wish(*names, msg):
    for n in names:
        print(msg, n)


greet("Hello", "Scott", "Tom", "Steve")
wish("Larry", "Sergy", "Great", msg="Hello")

print(10,20,sep =  ' * ',  end= '.')

