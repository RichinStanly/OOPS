#employee
#id,fname,lname,gender,dept,comp_name

class Employee:
    comp='Luminar'
    def setvalue(self,id,fname,lname,gender,dept):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.gender=gender
        self.dept=dept
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.gender,self.dept,Employee.comp)


employee1=Employee()
employee1.setvalue('101','sam','kevin','M','IT')
employee1.printvalue()

employee2=Employee()
employee2.setvalue('102','iron','man','M','physics')
employee2.printvalue()

employee3=Employee()
employee3.setvalue('103','dr','stranger','M','data science')
employee3.printvalue()

