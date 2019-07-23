inputlines=["CZ,Prague","CZ,Brno",'SK,Kosice',"CZ,Hradec Kralove",
            "FR,Paris",'DE,Berlin','FR,Lyon','SK,Trencin',"SK,Bratislava"]
cities={}
for row in inputlines:
  ccode,cname=row.split(',')
  try:
    cities[ccode].append(cname.strip())
  except KeyError:
    cities[ccode]=[cname.strip()]
for country in sorted(cities):
  print(country+': '+', '.join(sorted(cities[country])))
