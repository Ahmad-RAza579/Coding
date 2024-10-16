class Computer:
  def __init__(self):
    self.__maxprice=1000
  def sell(self):
    print("Selling price is",self.__maxprice)
  def setmaxprice(self,price):
    self.__maxprice =price
a=Computer()
a.sell()
a.__maxprice=2000
a.sell()
a.setmaxprice(2000)
a.sell()