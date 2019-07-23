inputlines=[" CZ ,Prague","CZ,  Brno",'SK, Kosice ',"CZ ,Hradec Kralove",
            "FR,Paris",'DE,Berlin','FR,Lyon','SK  ,Trencin ',"SK,Bratislava"]
cities={}
for row in inputlines:
  ccode,cname=[x.strip() for x in row.split(',')]
  #ccode=ccode.strip()
  #cname=cname.strip()
  if ccode in cities:
    cities[ccode].append(cname)
  else:
    cities[ccode]=[cname]
for country in sorted(cities):
  print(country+': '+', '.join(sorted(cities[country])))
