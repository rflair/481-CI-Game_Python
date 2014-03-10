# Example of object oriented programming

class Person(object):
    """ A person with attributes and methods """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):
        print("I am now walking!")
    def talk(self):
        print("Hello, I am a person!")

# main
person_a = Person("Robby", "15")
person_a.talk()
person_a.walk()
