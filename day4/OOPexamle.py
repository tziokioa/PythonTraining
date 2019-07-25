class Person:
    Person_id=1
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.cid=Person.Person_id
        Person.Person_id+=1

    def resetPerson(cls):
        cls.Person_id=1

    @classmethod
    def resetPerson(cls):
        cls.Person_id=1

    def printall(self):
        print ("Name : %s, age : %d, id : %d" % (self.name,self.age,self.cid))


pepa=Person("Josef",20)
lojza=Person("Alois",19)
janis = Person("Ioannis",45)
pepa.printall()

lojza.printall()
lojza.resetPerson()
janis.printall()