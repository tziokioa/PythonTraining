def greeting():
    """Documented Created by: Ioannis Tziokas"""
    print("Hello")


def add(a,b):
    """Sum of two numbers"""
    c=a+b
    return c

#action with multple actions
def addMultiply(a,b):
    return a+b, a*b

greeting()
x=add(1,2)
x2 = addMultiply(2,3)
print(x)
x3=add([1,3],[4,3])
print(x3)
print(sorted(x3))
print(x2)
print(type(x))
print(greeting.__doc__)