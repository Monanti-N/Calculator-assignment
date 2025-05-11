class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"

#polymorphism example
for animal in (Dog(), Cat()):
    print(animal.speak())        