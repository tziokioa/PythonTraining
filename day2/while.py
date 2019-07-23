a = 10
i = 1

while i<=a:
    print(i)
    i+=1
    while i == 5:
        print("{} Hello".format(i))
        i+=1

circumference = lambda r: 2*math.pi*r
circle_area = lambda r: math.pi*r**2
import math

while True:
    line = input('Enter radius in cm: ')
    if line.lower()=='quit':
        break
    if line.isdigit() and abs(int(line))>0:
        r=int(line)
        print(circumference(r))
        print(circle_area(r))
    else:
        print('Wrong value entered: ')
print('Program finished')