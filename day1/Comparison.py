# -*- coding: utf-8 -*-
import cmath
import math
a = 10
b = 11

kůň = "test"
print(kůň)

print(a == b)
print(a != b)

c = ~a
print(c)

comp_num = 5+4j
comp_num2 = 2+5.4j

num1 = cmath.sqrt(comp_num)
print(num1)


print(math.factorial(5))
num2 = 5*4*3*2*1
print(num2)

print(math.radians(180))
print(math.pi)


#calculate the surface of cirlce
r = 8
circle = 2*math.pi*r
print(circle, 'cm')
circle_surface = math.pi*r**2
print(circle_surface,'cm2')

bigVariable = """
Hello
World"""

print(bigVariable)
print(type(bigVariable))

print("Helloo Everyone\177\175")

print(r"hello\test\n\test")
print(u"hello test test")