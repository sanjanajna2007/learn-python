from random import randint
class train:
    def __init__(self, trainno):
        self.trainno = trainno   

    def book(self, fro, to):
        print(f"ticket is booked in trainno : {self.trainno} from{fro} to {to}")

    def checkstatus(self):
        print(f"train no: {self.trainno } is running on time")

    def getfare(self):
        print(f"ticket fare ijn train no {self.trainno} from {fro} to {to} is {randint(222, 12121)}")

t = train(12512)

t.book("hubli", "bangalore")
t.book("hubli", "mangalore")

        # getters and setters
class student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    

s = student("sabjana", 18)
print(s.get_name())
s.set_name("sanju")
print(s.get_name())

#  method overloading

class calculator:
    def add(self, a, b):
        print(a + b ) 

c = calculator()
c.add(1,2)

#  super class

class animal:
    def make_sound(self):
        print("animal making sound which is")

class dog(animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        super().make_sound()
        print(f"{self.name} is barking")

    def get_angry(self):
        super().make_sound()
        self.make_sound

d = dog("doggyy")
d.make_sound()

     # abstraction
 
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def strat_engine(self):
        pass

class bike(vehicle):
    def __init__(self,name):
        self.name = name

    def strat_engine(self):
        print("starting engin")

b = bike("royal enfield")
print(b.name)

class bankaccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance

    def set_balace(self, balance):
        if balance >=0:
            self.__balance = balance

        else:
            print("you balance cannot be zero")
account = bankaccount(1000)
print(account.get_balance)

account.set_balace(20000)
print(account.get_balance)

account.set_balance(-12)
print(account.get_balance)