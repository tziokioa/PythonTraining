import mymodule as m
import sys
cities={}
try:
  file=open(sys.argv[1],"r")
except IndexError:
  print('No filename specified')
  exit(2)
except:
  print("Some error occured opening file")
  exit(1)
for row in file:
  ccode,cname=m.process_row(row)
  if ccode is None:
    continue
  if ccode in cities:
    cities[ccode].append(cname)
  else:
    cities[ccode]=[cname]
file.close()
for country in sorted(cities):
  print(country+': '+', '.join(sorted(cities[country])))
