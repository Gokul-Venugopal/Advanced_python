
class Person:
    number_of_people=0
    def __init__(self,name):
        self.name=name
        Person.number_of_people=Person.number_of_people + 1
        #number_of_people is accesed using Person

p =Person("Ram")
p.name
print(p.number_of_people)
p =Person("Bheem")                       #second name is pushed and number is incremented to 2
print(p.number_of_people)

################################################################################################################
class Person:
    number_of_people=0
    def __init__(self,name):
        self.name=name
        Person.number_of_people=Person.number_of_people + 1

    @classmethod                       ## @classmethod  delclaration is mandatory to access using cls
    def get_number(cls):               ##accessing the number_of_people using cls object
        return cls.number_of_people

d1=Person("Sam")
d2=Person("Tim")
print(Person.get_number())

#using static method
class Math:

    @classmethod
    def add_method(cls):
        return cls.x+10
    @staticmethod                   #using staticmethod
    def mul_method(self):
        return x*3

#################################################################################################################
#memory management
x=10
y=x
print(id(x))      # both x and y values are stored in same memory location 1645102721616
print(id(y))       #it manages space like this
if id(x)==id(y):
    print("same memory location")
else:
    print("no same memory location")

#################################################################################################################
import sys
print(sys.getsizeof(x))    ## it occupies 28 bytes because python has overheads such as reference of the pointer
                           ##,type etc and thus occupies more space
str=''
print(sys.getsizeof(str))  ##49 bytes including overheads
str='h'
print(sys.getsizeof(str))  ##50 bytes that means one character + 49 overhead bytes
str='hell0'
print(sys.getsizeof(str))   ## 54 bytes i.e 49+5

list1=[]
print(sys.getsizeof(list1))  #56 bytes
list1=[1]
print(sys.getsizeof(list1))  #64 bytes   56+8

tup=()                      #40 bytes
print(sys.getsizeof(tup))
tup=(1,2)                   #40 +8+8=56
print(sys.getsizeof(tup))

################################################################################################################