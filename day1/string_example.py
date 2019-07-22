import math
#calculate the surface of cirlce
r = 8
o = 2*math.pi*r
circle_surface = math.pi*r**2
# print('{} of circle with radius {} is {:6.6} cm'.format('Circumference',r,o))
#
# print('{:>15} of circle with radius {} is {:>6.6} cm2'.format('Circle area',r,circle_surface))



message='{:>15} of circle with radius {} is {:6.6} {}'
print(message.format('Circumference',r,o,'cm'))
print(message.format('Circle area',r,circle_surface,'cm2'))

