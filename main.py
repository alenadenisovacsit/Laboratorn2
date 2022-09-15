def decor1(func):
    def wrapper1():
        print('Всем')
        func()
    return wrapper1
def f1():
    print('Привет')
f1 = decor1(f1)
f1()

def decor2(func):
    def wrapper2(a):
        return func(a)/2
    return wrapper2
@decor2
def f2(a):
    return a*a*a
print(f2(5))

def decor3(func):
    def wrapper3(a):
        return 1/func(a)
    return wrapper3
@decor3
@decor2
def f3(a):
    return a+2
print(f3(9))



