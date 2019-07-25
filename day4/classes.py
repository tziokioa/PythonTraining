class Person():
    def printall(self):
        print("Name:  {}, Age: {}, Work: {}".format(self.name,self.age,self.ocup))


jan = Person()
jan.name="Ioannis"
jan.age=20
jan.ocup="Worker"
x=Person()
x.name="Alexandros"
x.age=23
x.ocup="Worker"

del jan.name
jan.printall()
x.printall()
print(dir(jan))

