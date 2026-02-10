#constructor

class Person:
    def __init__(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age)

person1=Person(101,'vinay','k',30)
person1.printvalue()

person2=Person(102,'wanda','vision',30)
person2.printvalue()