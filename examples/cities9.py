inputlines=[" CZ ,Prague","CZ,  Brno",'SK, Kosice ',"CZ ,Hradec Kralove",
            "FR,Paris",'DE,Berlin','FR,Lyon','SK  ,Trencin ',"SK,Bratislava",
            "CZ,","SK:Zilina","CZ Pardubice","A,B","Cz,Kladno"]
cities={}
import mymodule as m
for row in inputlines:
  ccode,cname=m.process_row(row)
  if ccode is None:
    continue
  if ccode in cities:
    cities[ccode].append(cname)
  else:
    cities[ccode]=[cname]
for country in sorted(cities):
  print(country+': '+', '.join(sorted(cities[country])))
