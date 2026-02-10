#Encapulation
#binding of data and methods
#helps to hide data


class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

p = Person("John")
print(p.get_name())
p.set_name("Mike")
print(p.get_name())
