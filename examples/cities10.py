import mymodule as m
cities={}
try:
  file=open("cities.txt","r")
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
