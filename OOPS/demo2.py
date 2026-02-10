class Person:
    def setvalue(self,first_name,last_name,age,gender,phno):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.phno=phno
    def printvalue(self):
        print(self.first_name,self.last_name,self.age,self.gender,self.phno)

person1=Person()
person1.setvalue('vinay','k',26,'male',12345)
person1.printvalue()
print("*"*100)
person2=Person()
person2.setvalue('anu','p',30,'male',1234567)
person2.printvalue()
person3=Person()
person3.setvalue('sam',"zammy",23,'male',1234567)
person3.printvalue()