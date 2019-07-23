import os

def clean_screen():
    if os.name == 'nt':
        os.system('cls')
        print()
    else:
        os.system('clear')
        print("\n\n")

def process_row(line,sep=","):
    L=line.split(sep)
    if len(L) !=2:
        return (None,None)
    my_ccode,my_cname=[x.strip() for x in L]
    if len(my_ccode) !=2 or len(my_cname) <=1:
        return (None,None)
    return (my_ccode.upper(),my_cname)


inputlines = ["CZ,Prague","SK, Trencin", "CZ,Brno", 'SK,Kosice', "CZ,Hradec Kralove", "FR,Paris", 'DE,Berlin', 'FR,Lyon',
              'SK,Trencin',"cz,", "gr", "DE,        berlin", "SK,Bratislava","     CZ, Prague"," CZ,Prague"]


cities = {}
debug = False
clean_screen()
for row in inputlines:

    if debug:
        print(row)

    ccode, cname = process_row(row)

    # ccode,cname=process_row(row)

    if debug:
        print('State is:', ccode, 'city name is:', cname)
    try:
        cities[ccode].append(cname)
    except:
        cities[ccode] = [cname]
if debug:
    print(cities)

final_countries = [ print(country + ': ' + ', '.join(set(sorted(cities[country])))) for country in sorted(cities)]

