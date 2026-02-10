#student
#id,fname,lastname,course,gender,coll_name

#5 obj
#instance variable
#static variable

class Student:
    coll='MES'
    def setvalue(self,id,fname,lname,gender,course):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.course=course

    def printvalue(self):
        print(self.id,self.fname,self.lname,self.gender,self.course,Student.coll)

student1=Student()
student1.setvalue(1,'vinay','k','female','btech')
student1.printvalue()

student2=Student()
student2.setvalue(2,'sam','t','male','cs')
student2.printvalue()

student3=Student()
student3.setvalue(3,'vinu','j','male','mech')
student3.printvalue()

student4=Student()
student4.setvalue(4,'riya','J','female','bca')
student4.printvalue()

student5=Student()
student5.setvalue(5,'prashob','p','male','btech')
student5.printvalue()