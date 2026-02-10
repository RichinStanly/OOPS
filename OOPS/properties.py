#

#1. Inheritance
#2. Polymorphism
#3. Abstraction
#4.Encapsulation


#1.Inheritance

class A: #parent  Base class
    def printa(self,num1):
        self.num1=num1
        print("Inside class A",self.num1)

class B(A): #child derved classs
    def printb(self,num2):
        self.num2=num2
        print("Inside class B",self.num2)

obj1=B()
obj1.printb(10)
obj1.printa(20)