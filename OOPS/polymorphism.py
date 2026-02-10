#polymorphism

#many forms
#helps on method overloading and method overriding


class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Dog Bark")

class Cat(Animal):
    def sound(self):
        print("Cat Meow")

for animal in (Dog(), Cat()):
    animal.sound()
