# -*- coding: utf-8 -*-
import math
r=8
#o=2*3.14259*r
o=2*math.pi*r
message='{:>15} of circle with radius {} is {:6.6} cm'
print(message.format('Circumference',r,o))
a=math.pi*r**2
print(message.format('Circle area',r,a))
