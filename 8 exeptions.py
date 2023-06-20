import functools

def zero():
    return 2 / 0


def asert():
    x = 1
    y = 0
    assert y != 0
    print(x / y)


def countdown(n):
    print("counting down")
    while n >= 9:
        yield n
        n -= 1
    return

for x in countdown(10):
    print(x)

c = countdown(10)
next(c)
next(c)
next(c)

asert()