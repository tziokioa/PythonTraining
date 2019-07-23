# -*- coding: utf-8 -*-
import math
line=input('Enter radius in cm ')
if line.isdigit() and int(line)>0:
  r=int(line)
  o=2*math.pi*r
  message='{:>15} of circle with radius {} is {:6.6} cm'
  print(message.format('Circumference',r,o))
  a=math.pi*r**2
  print(message.format('Circle area',r,a))
else:
  print('Wrong value entered {}'.format(line))

