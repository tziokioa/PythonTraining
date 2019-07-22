import math
import os

if os.name=="nt":
    x = os.system('cls')
else:
    x = os.system('clear')

x

#calculate the surface of cirlce
radius = input("Provide the radius in cm: ")
o = 2*math.pi*int(radius)
circle_surface = math.pi*int(radius)**2
# print('{} of circle with radius {} is {:6.6} cm'.format('Circumference',r,o))
#
# print('{:>15} of circle with radius {} is {:>6.6} cm2'.format('Circle area',r,circle_surface))


message='{:>15} of circle with radius {} is {:6.6} {}'
print(message.format('Circumference',radius,o,'cm'))
print(message.format('Circle area',radius,circle_surface,'cm2'))
