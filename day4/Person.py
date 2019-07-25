class Person:
    def __init__(self, name='',age=0):
        self.name=name
        self.age=age

    def __str__(self):
        return(self.name)

    def __gt__(self,other):
        if (self.age>other.age):
            return True
        return False

    def __add__(self,other):
        return self.age+other.age

    def printall(self):
        print("Name: {}, Age: {}".format(self.name, self.age))