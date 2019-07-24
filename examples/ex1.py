i=10
#file=open(...)
print("open file")
try:
  #raise KeyboardInterrupt
  j=i/0
except (ZeroDivisionError):
  print('Exception raised ')
except KeyboardInterrupt:
  print('keyboard')
print('finishing program')
