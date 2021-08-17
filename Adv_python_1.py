#Object Oriented Programming
##################################################################################################################
#type values
x=1
print(type(x))      #integer value is an object of type class int
y='c'
print(type(y))

tuple1=(1,3,5)
print(type(tuple1))  #tupule1 is an object of type class tuple

def function():
    print("This is a sample function")
print(type(function))  #function type class

print(1+2)           #'+' operator can be used for arithmatic addition
str='hello'
print(str+'bye')     #'+' operator can also be used for string concatination

################################################################################################################
class Car_Info:
 def __init__(self,name,model_name,color):     #constructor of a class
     self.name=name                      #class data initialzed
     self.model_name=model_name
     self.color=color
 def drive_car(self):
     print(f'The {self.name} {self.model_name} is running on the street')
 def car_color(self):
     print(f'The {self.name} {self.model_name} color is {self.color}')


run=Car_Info('lamborghini','Gallardo','black')      # run is the object of class car
print(f'Name -{run.name}')             #acessing the class data
print(f'Model-{run.model_name}')
run.drive_car()                        #drive_car is accesed using run object
run.car_color()                        #car_color is accesed using run object

print(type(run))                       #the datatype of run  <class '__main__.Car'>
print(type(run.name))                  #the datatype of name  <class 'str'>


#using second object run2

run2=Car_Info('Aston Martin','Valkyrie Spider','green')
print(f'Name -{run2.name}')             #acessing the class data
print(f'Model-{run2.model_name}')
run2.drive_car()                        #drive_car is accesed using run object
run2.car_color()                        #car_color is accesed using run object








