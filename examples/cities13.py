import sys
import re
cities={}
if len(sys.argv)!=2:
  print("wrong args")
  exit(3)
try:
  file=open(sys.argv[1],"r")
except IndexError:
  print('No filename specified')
  exit(2)
except:
  print("Some error occured opening file")
  exit(1)
myreg=re.compile('^ *([A-Z]{2}) *, *([A-Z][a-z].*) *$')
for row in file:
  m=myreg.search(row)
  if m:
    ccode,cname=m.groups()
    if ccode in cities:
      cities[ccode].append(cname)
    else:
      cities[ccode]=[cname]
file.close()
for country in sorted(cities):
  print(country+': '+', '.join(sorted(cities[country])))
