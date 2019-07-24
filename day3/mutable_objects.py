def example (n,list1, list2):
    """Mutable Objects"""
    list1.append('Black')
    list2=[3,2,1]
    n+=1
    print(n)
    print(list1)
    print(list2)


a=7
b=['Joe']
c=[4,8,9]
example(a,b,c)
print()
print(example.__doc__)
print(a)
print(b)
print(c)