import mymodule as m
import sys
import os
import pickle
pfname='cities.pickle'
cities={}
#check for existence of pickle file with cities
if os.path.isfile(pfname):
  pf=open(pfname,"rb")
  cities=pickle.load(pf)
  pf.close()
for f in sys.argv[1:]:
  try:
    file=open(f,"r")
  except:
    print("Some error occured opening file "+file)
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
#store as pickle
pf=open(pfname,"wb")
pickle.dump(cities,pf)
pf.close()
