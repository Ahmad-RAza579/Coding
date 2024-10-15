class dad:
    def __init__(self,eyes,aggressive):
        self.eyes = eyes
        self.aggresive = aggressive
    def display(self):
        print("your eye colour is", self.eyes)
        print("you are aggresive", self.aggresive)

class son(dad):
    def __init__(self,name,age,eyes,agressive):
        self.name = name
        self.age = age
        dad.__init__(self,eyes,agressive)
obj = son("penguin", 8, "blue", True)
obj.display()
