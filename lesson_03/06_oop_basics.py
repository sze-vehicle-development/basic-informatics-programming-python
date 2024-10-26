class Dog:
    def __init__(self, name):
        self.name = name
my_dog = Dog('Doggie')
print(my_dog.name)
# Example #2
# Class with a method
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return 'Woof!'
my_dog = Dog('Doggie')
print(my_dog.bark())