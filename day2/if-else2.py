import math
circumference = lambda r: 2*math.pi*r
circle_area = lambda r: math.pi*r**2
line=input('Enter radius in cm ')
if line.isdigit()and int(line) > 0:
    r=int(line)
    print(circumference(r))
    print(circle_area(r))
else:
    print("Wrong value entered")
