import os

if os.name == 'nt':
    os.system('cls')
    print()
else:
    os.system('clear')
    print("\n\n")

inputlines = ["CZ,Prague","SK, Trencin", "CZ,Brno", 'SK,Kosice', "CZ,Hradec Kralove", "FR,Paris", 'DE,Berlin', 'FR,Lyon',
              'SK,Trencin', "SK,Bratislava","     CZ, Prague"," CZ,Prague"]

inputlines.append("GR,Athens")

cities = {}

debug = False

for row in inputlines:

    if debug:
        print(row)

    ccode, cname = [x.strip() for x in row.split(',')]

    if debug:
        print('State is:', ccode, 'city name is:', cname)
    try:
        cities[ccode].append(cname)
    except:
        cities[ccode] = [cname]
if debug:
    print(cities)

final_countries = [ print(country + ': ' + ', '.join(set(sorted(cities[country])))) for country in sorted(cities)]

# for country in sorted(cities):
#     print(country + ': ' + ', '.join(set(sorted(cities[country]))))

# print(final_countries)