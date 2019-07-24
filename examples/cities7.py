inputlines=[" CZ ,Prague,1_000_000","CZ,  Brno,400_000",'SK, Kosice,280_000 ',"CZ ,Hradec Kralove,120_000",
            "FR,Paris,6_200_000",'DE,Berlin,4_350_000','FR,Lyon,1_200_000','SK  ,Trencin,25000',"SK,Bratislava,510_000"]

cities={}
for row in inputlines:
  ccode,cname,pop=[x.strip() for x in row.split(',',2)]
  pop=int(pop)
  if ccode in cities:
    cities[ccode].append((cname,pop))
  else:
    cities[ccode]=[(cname,pop)]
for country in sorted(cities):
  print(country+': '+', '.join(x[0] for x in sorted(cities[country],key=lambda x:x[1],reverse=True)))
