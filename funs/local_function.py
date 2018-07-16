gv = 10


def fun1():
    ev = 20

    # local function
    def fun2():
        lv = 30
        nonlocal ev
        global gv
        gv += 10
        ev = ev + 1
        # gv = 100
        print(gv, ev, lv)  # Global, enclosing, local

    fun2()  # call fun2
    print(ev)


fun1()
print(gv)


