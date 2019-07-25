from Person import Person
import pickle


janis=Person("Ioannis", 30)
janis.ocup="Worker"
janis.printall()
print(str(janis))
alex = Person("Alex",29)
print(janis>alex)
print(janis+alex)

myfile=open("dataDump.txt","ab")
pickle.dump(janis,myfile)
pickle.dump(alex,myfile)
myfile.close()