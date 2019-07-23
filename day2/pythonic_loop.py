# old style:
L1 = list(range(0,20,3))
L3 = [x*2 if x%2==0 else x for x in L1]
print(L3)


print("""
for i in L1:
    if i%2==0:
        L2.append(i*2)
    else:
        L2.append(i)
""")