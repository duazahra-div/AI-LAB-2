class Person:
    def __init__(self,name,age):
     self.name=name 
     self.age=age
def my_func(self):
       print("Hello my name is " + self.name)

p1=Person("John",36)
my_func(p1)