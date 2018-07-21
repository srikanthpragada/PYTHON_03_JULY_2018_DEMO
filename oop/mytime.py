class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @classmethod
    def create(cls, value):
        return cls(value, value, value)

    @staticmethod
    def validate(h, m, s):
        if h < 0 or h > 23:
            return False
        if m < 0 or m > 59:
            return False
        if s < 0 or s > 59:
            return False
        return True

    def __str__(self):
        return f"{self.h}:{self.m}:{self.s}"

    @property
    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    @totalseconds.setter
    def totalseconds(self, value):
        print("Setting totalseconds to ", value)

    def __add__(self, secs):
        if isinstance(secs, int):
            return Time(self.h, self.m, self.s + secs)
        else:
            return self


t = Time.create(10)
print(t)

print ( Time.validate(30,20,30))

