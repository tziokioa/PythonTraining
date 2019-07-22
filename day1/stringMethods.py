import string
text = "Hello World"
print(text)

print(text[0:5])
print(text[6:])
print(text[::2])

print(ord('A'))
print(chr(123))
test2 = 'příšera'.encode('utf-8')
test3 = test2.decode('utf-8')
print(test2)
print(test3)
b = len(text)
print(b)


number_1 = 123
number_2 = '123'
print(int(number_2))
number_4 = '123.123'
print(float(number_4))
number_5 = '1+5j'
print(complex(number_5))



x=string.Template('$ham and $eggs')
print(dir(x))
print(x.substitute(ham='sunka', eggs='vajicka'))

x = 'this is a very very very very long string'
print(x.count('very'))

print(x.endswith('very'))
print(x.endswith('very',0,14))

L2='This is a string'.split()
