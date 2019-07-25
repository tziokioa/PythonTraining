import re
re.search('o','Ahoj')


if re.search('j','ahoj'):
    print("found o")

myreg=re.compile(r'^(.).*\1$')
print(myreg.match('ahoja'))