# class MyClass():
#   x = 5
# p = MyClass()
# print(p.x)




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("Emil", 36)
#
# print(p1.name,p1.age)
# print(p1.age)




# class Car:
#   def __init__(self,name,brand,year):
#     self.name = name
#     self.brand = brand
#     self.year = year
# car = Car("Lexus","Toyota",2022)
# print(car.name,car.brand,car.year)





# Methods are functions that belong to a class. They define the behavior of objects created from the class.
# ExampleGet your own Python Server
# Create a method in a class:
#
# class Person:
#   def __init__(self, name):
#     self.name = name
#
#   def greet(self):
#     print("Hello, my name is " + self.name)
#
# p1 = Person("Emil")
# p1.greet()





# Methods can accept parameters just like regular functions:
#
# Example
# Create a method with parameters:
#
# class Calculator:
#   def add(self, a, b):
#     return a + b
#
#   def multiply(self, a, b):
#     return a * b
#
# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))



# Example
# A method that accesses object properties:
#
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def get_info(self):
#     return f"{self.name} is {self.age} years old"
#
# p1 = Person("Tobias", 28)
# print(p1.get_info())


# Methods can modify the properties of an object:\
# Example
# A method that changes a property value:


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def celebrate_birthday(self):
#     self.age += 1
#     print(f"Happy birthday! You are now {self.age}")
#
# p1 = Person("Linus", 25)
# p1.celebrate_birthday()
# p1.celebrate_birthday()