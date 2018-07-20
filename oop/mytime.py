class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h}:{self.m}:{self.s}"

    @property
    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    @totalseconds.setter
    def totalseconds(self,value):
        print("Setting totalseconds to ", value)


t1 = Time(m=10, s=20)
t1.totalseconds = 100
print(t1.totalseconds)
