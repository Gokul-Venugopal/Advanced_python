#A python script is called a Module
#These modules are grouped together for a package
#Interpreter recognizes a file as a package if it has a __init__.py file in it
#User can make his own packages and import it
from package1.MainModule import is_prime
from package1.MySubPackage.Submodule import is_even
print(is_prime(13))                         #is_prime recognizes if a number is prime or not

is_even(188)                                 #is_even to check for an even number



