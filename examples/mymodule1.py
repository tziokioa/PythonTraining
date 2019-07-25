"""This is my first module:)
Use it for cities/countries programs
have fun:)"""
a=10
_b=20
_gopas="hello world"
#print("sfsfsfsfsdf")
def process_row(line,sep=","):
  """Function process row is one one in this module"""
  L=line.split(sep)
  if len(L)!=2:
    return (None,None)
  my_ccode,my_cname=[x.strip() for x in L]
  if len(my_ccode)!=2 or len(my_cname)<=1:
    return (None,None)
  #print(_gopas)
  return (my_ccode.upper(),my_cname)

def main():
  print("This is our script !!!")
  print(process_row('CZ,Prague'))

if __name__ == '__main__':
  main()
