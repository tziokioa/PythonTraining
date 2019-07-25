# -*- coding: utf-8 -*-
import math
class Circle:
  def __init__(self,radius):
    self.radius=int(radius)
  def area(self):
    return math.pi*self.radius**2
  def circumference(self):
    return 2*math.pi*self.radius
  def __str__(self):
    return str(self.radius)

while True:
  line=input('Enter radius in cm ')
  if line.lower()=='quit':
    break
  if line.isdigit() and int(line)>0:
    c=Circle(line)
    message='{:>15} of circle with radius {} is {:6.6} cm'
    print(message.format('Circumference',c,c.circumference()))
    print(message.format('Circle area',c,c.area()))
  else:
    print('Wrong value entered {}'.format(line))
print('Program finished')

