inputlines=[" CZ ,Prague","CZ,  Brno",'SK, Kosice ',"CZ ,Hradec Kralove",
            "FR,Paris",'DE,Berlin','FR,Lyon','SK  ,Trencin ',"SK,Bratislava",
            "CZ,","SK:Zilina","CZ Pardubice","A,B","Cz,Kladno"]
cities={}
def process_row(line,sep=","):
  L=line.split(sep)
  if len(L)!=2:
    return (None,None)
  my_ccode,my_cname=[x.strip() for x in L]
  if len(my_ccode)!=2 or len(my_cname)<=1:
    return (None,None)
  return (my_ccode.upper(),my_cname)

for row in inputlines:
  ccode,cname=process_row(row)
  if ccode is None:
    continue
  if ccode in cities:
    cities[ccode].append(cname)
  else:
    cities[ccode]=[cname]
for country in sorted(cities):
  print(country+': '+', '.join(sorted(cities[country])))
