def maximum(*numbers):
    m=numbers[0]
    if m==0:
        pass
    else:
        for n in numbers[1:]:
            if n>m:
                m=n
        return m

print(maximum(1,4,5,11,0,2,51))

def cityNames(**params):
    for i in params:
        print("Name of City is {} and value is {}".format(i,str(params[i])))

cityNames(cz='Prague',sk='Bratislava')