class bird:
    print("i am a bird")
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    
    def display(self):
        print("my name is",self.name)
        print("and my colour is",self.colour)

a=bird("parrot","yellow")
a.display()