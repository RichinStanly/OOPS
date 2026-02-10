#class person :fname,lname,age,location
#class professional :id,fname,lastname,age,dept,qualification,location


class Person:
    def printa(self,fname,lname,age,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.location=location

class Proff(Person):
    def printb(self,id,dept,qualification):
        self.id=id
        self.dept=dept
        self.qualification=qualification

    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.dept,self.qualification,self.location)


person=Proff()
person.printa('Iron','man',40,'america')
person.printb(101,'IT','CS')
person.printvalue()
