def fun3(**kwargs):
    print(kwargs)
    print(len(kwargs))
    print(kwargs.keys())

fun3(a=12,b="Hekki")


def fun3(a,b,c=33,*var1,**var2):
    print(a)
    print(b)
    print(c)
    print(var1)
    print(var2)

fun3(10,"hello")