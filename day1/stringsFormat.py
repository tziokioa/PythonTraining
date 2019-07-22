a=10
print("Variable has value %d" % a)

x = 'Hello %s capacity'%'world'
print(x)
x = 'Hello %10s capacity'%'world'
print(x)
x = 'Hello %-10s capacity'%'world'
print(x)

x = 'Hello %-10s capacity %f'%('world',123)
print(x)

#New Method:
text = "ioannis"
text2 = "Tzikas"

print("Value is {0} and {1}".format(text,text2))
print("Value is {0:>10} and {1:<20} test test ".format(text,text2)) #spacing
print("Value is {0:.>10.6} and {1:<20} test test ".format(text,text2)) #spacing
print("Value is {0:^10} and {1:^20} test test ".format(text,text2)) #center text between the space
print("Value is {0:^10} and {2:.3} test test ".format(text,text2,123.0))

#new in python3.6
text3 = "text1"
text4 = 123
print("Value is {0} and {1}".format(text3,float(text4)))
print(f"Value is {text3} and {text4}")

print("Value is {aa} capacity {bb}".format(aa=a,bb=text3))

type(text) #type of variable
id(text) #memory id of varibable

text="         hello test example example fix example test"


print(text.title().find('Example',14))

print(text.split())

phrase = text.split()
print(phrase[2])

print(text.split(' '))