
#OOPS Concept in Python:
#Classes and objects
class ECE_Student:
    # Class Variable
    stream = 'ECE'

    #  constructor
    def __init__(self, roll_no):
        # Instance Variable
        self.roll = roll_no

a = ECE_Student(101)        #instatiation
b = ECE_Student(102)

print(a.stream)  # prints ECE
print(b.stream)  # prints ECE
print(a.roll)  # prints 101

# Class variables can be accessed using class
# name also
print(ECE_Student.stream)  #prints ECE

##############################################################################################################
#Inheritance
# parent class
class Bird_Class:

    def __init__(self):
        print("Bird is ready")

    def name_bird(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Pegion(Bird_Class):  #Pegion inherits from Bird_Class

    def __init__(self):
        # call super() function
        super().__init__()
        print("Pegion is ready")

    def bird_name(self):
        print("Pegion")

    def run(self):
        print("Run faster")


birdy = Pegion()
birdy.bird_name()
birdy.swim()
birdy.run()

#############################################################################################################
#Data Encapsulation
class Machine:

    def __init__(self):
        self.__maxprice = 900    #we can set private variables with '_' and '__'

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Machine()
c.sell()

# change the price
c.__maxprice = 1000    #we are trying to change the value of selling price but as
c.sell()               # they are private variables its not possible

# only using member function we can change
c.setMaxPrice(1000)
c.sell()

##############################################################################################################
#Polymorphism
#Method overriding
class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Rabbit (Parrot):

    def fly(self):
        print("Rabbit can't fly")

    def swim(self):
        print("Rabbit can swim")


p=Parrot()                   #Baseclass and subclass have the same fuctions
p.fly()
p=Rabbit()
p.swim()                      #When swim function is called using the same object the subclass
                              #overrides the base class

##############################################################################################################
#Data Abstaction:

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self,name):
        self.name = name

    def description(self):
        print("This the description function of class car.")

    @abstractmethod
    def price(self,x):         #Abstraction: implimentation details are not disclosed
        pass
class Child_Car(Car):
    def price(self,x):
        print(f"The {self.name}'s price is {x} lakhs.")

obj1 = Child_Car("Aston Martin")

obj1.description()
obj1.price(80)

#############################################################################################################