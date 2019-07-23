inputlines=["CZ,Prague","CZ,Brno",'SK,Kosice',"CZ,Hradec Kralove",
            "FR,Paris",'DE,Berlin','FR,Lyon','SK,Trencin',"SK,Bratislava"]
cities={}
for row in inputlines:
  ccode,cname=row.split(',')
  if ccode in cities:
    cities[ccode]+=', '+cname
  else:
    cities[ccode]=cname
#print(cities)
for country in sorted(cities):
  print(country+': '+cities[country])
