inputlines=["CZ,Prague","CZ,Brno",'SK,Kosice',"CZ,Hradec Kralove",
            "FR,Paris",'DE,Berlin','FR,Lyon','SK,Trencin',"SK,Bratislava"]
cities={}
debug=True
for row in inputlines:
  if debug:
    print(row)
  ccode,cname=row.split(',')
  if debug:
    print('State is:',ccode,'city name is:',cname)
  if ccode in cities:
    cities[ccode]+=', '+cname
  else:
    cities[ccode]=cname
if debug:
  print(cities)
for country in sorted(cities):
  print(country+': '+cities[country])
