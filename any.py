from abc import ABC
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move (self):
        print("human walk with 2 legs")
class Snake(Animal):
    def move(self):
        print("snake crawl with their body")
a=Animal()
b=Human()
b.move()
c=Snake()
c.move()
