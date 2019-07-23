num1 = input("Give me a number: \n ")
num2 = input("Give me a second number: \n")
message = "{} is bigger than {}"

print("You gave numbers {} and {}".format(num1, num2))

# if num1>num2 :
#     print(message.format(num1,num2))
# elif num2>num1 :
#     print(message.format(num2, num1))
# else :
#     print("Numbers are equal")


if num1>num2 :
    pass
elif num2>num1 :
    print(message.format(num2, num1))
else :
    print("Numbers are equal")

i=0
while i <= 10:
    i+=1
    print(i)