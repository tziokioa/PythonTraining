inputlines=[" CZ ,Prague,1_000_000","CZ,  Brno,15_5000",'SK, Kosice,122_000 ',"CZ ,Hradec Kralove,15_0000",
            "FR,Paris,40_000",'DE,Berlin,550_000','FR,Lyon,450_000','SK  ,Trencin,544_000 ',"SK,Bratislava,23_121_990"]
cities={}
for row in inputlines:
  ccode,cname,cpop=[x.strip() for x in row.split(',',2)]
  #ccode=ccode.strip()
  #cname=cname.strip()
  pop=int(cpop)
  if ccode in cities:
    cities[ccode].append((cname,pop))
  else:
    cities[ccode]=[(cname,pop)]

for country in sorted(cities):
  print(country+': '+', '.join(x[0] for x in sorted(cities[country],key=lambda x:x[1],reverse=True)))
print()
for country in sorted(cities):
  print(country+' '+', '.join(x[0] +' Population :'+ str(x[1]) for x in sorted(cities[country],key=lambda x:x[1],reverse=True)))
# for country in sorted(cities):
#   print(country+': '+', '.join(sorted(cities[country])))
