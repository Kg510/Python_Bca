71)
# WAP to create add function that takes 2 parameters 

def add(a,b):
    return a+b
result= add(10,20)
print(result)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

72)
# WAP to create a default function 

def greet(name="guest"):
    print(f"Hello,{name}!")
greet()
greet("Kunal")
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

73)
# WAP to demonstrate multiple return using function

def get_user_info():
    name = "Alice"
    age = 30
    return name,age
user_name , user_age = get_user_info()
print(user_name)
print(user_age)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

74)
# WAP to return list through function
def get_squares(numbers):
    squares = [n**2 for n in numbers]
    return squares
nums = [1,2,3,4]
squares_list = get_squares(nums)
print(squares_list)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

75)
# Write a Python program to demonstrate Conditional returns

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result = check_even_odd(4)
print(result)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

76)
# Write a Python program to demonstrate early exit with return

def find_first_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            return n
        return None
nums = [1,3,5,8,9]
first_even = find_first_even(nums)
print(first_even)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

77)
# Write a Python program to demonstrate No explicit return

def greet(name):
    print(f"Hello,{name}")
result = greet("Kunal")
print(result)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")


78)
# Wap to demonstrate different types of parameters

# Positional Parameters
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    
greet("Alice", 30)
print("This is the result for Positional Parameters.\n")


# Default Parameters
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")
    
greet("Alice")
print("This is the result of Default Parameters.\n")


# Keyword Parameters
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")
    
greet(name="Alice", age=30)
print("This is the result of Keyword Parameters.")

# Variable-length Parameters

# Using *args for variable number of arguments (positional arguments)
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))
print(sum_numbers(4, 5, 6, 7, 8))
print("This is the result for *args (variable-length positional parameters).\n")


# Using **kwargs for variable number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
print("This is the result for **kwargs (variable-length keyword parameters).")
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")


79)
#Wap in py to demonstrate decorators 
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        # Add functionality before calling the original function
        result = original_function(*args, **kwargs)
        # Add functionality after calling the original function
        return result
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")


80)
#Wap in py to demonstrate decorators with arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Kunal")
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")


81)
#Wap in py to check user permissions using  decorators
import functools

def get_current_user_permissions():
    return ['admin', 'editor']

def requires_permission(permission):
    def decorator(func):
        @functools.wraps(func)  # This will preserve the original function metadata
        def wrapper(*args, **kwargs):
            user_permissions = get_current_user_permissions()  # Get current user permissions
            if permission in user_permissions:  # Check if the user has the required permission
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have permission to access this resource.")
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user_id):
    print(f"User {user_id} deleted")
        
try:
    delete_user(123)
except PermissionError as e:
    print(e)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")


82)
#WAP in py to demonstare how decorators work

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

83)
# WAP to  demonstrate Math Utils

def add(x, y):
    return x + y

def subtract(x, y):
    return x – y
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

84)
# WAP to Using a Module
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

result = add(5, 3)
print(result)  # Output: 8
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")


85)
# WAP for importing specific function
def add(x, y):
    return x + y

result = add(5, 6)
print(result)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

86)
# WAP for importing all function
def subtract(x, y):
    return x - y

result = subtract(10, 8)
print(result)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

87)
# WAP to demonstrate aliasing module and functions
def add(x, y):
    return x + y

result = add(5, 45)
print(result)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

88)
# Question 88: Importing Modules Dynamically
def add(x, y):
    return x + y

result = add(15, 30)
print(result)  
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")


89)
# WAP to demonstrate class, object, properties and methods
class Car: 
    def _init_(self, make, model, year): 
        self.make = make
        self.model = model 
        self.year = year 
    def display_info(self): 
        print(f"{self.year} {self.make} {self.model}")
my_car = Car("Toyota", "Corolla", 2020) 
my_car.display_info()
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")
90)
# WAP to demonstrate Encapsulation
class Car:
    def _init_(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
    
    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")
    
    def set_year(self, year):
        if year > 1885:
            self._year = year
        else:
            print("Invalid year")
    
    def _str_(self):
        return f"{self._year} {self._make} {self._model}"

car = Car("Tesla", "Model S", 2023)
car.display_info()
car.set_year(1880)
car.set_year(2025)
print(car)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

91)
# WAP to demonstrate Inheritance
class Vehicle: 
    def _init_(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year
    
    def display_info(self): 
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle): 
    def _init_(self, make, model, year, fuel_type): 
        super()._init_(make, model, year)
        self.fuel_type = fuel_type
    
    def display_info(self): 
        super().display_info()
        print(f"Fuel type: {self.fuel_type}")

my_car = Car("Toyota", "Corolla", 2020, "Petrol")
my_car.display_info()
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

92)
# WAP to demonstrate Polymorphism
class Animal: 
    def speak(self): 
        pass 
class Dog(Animal): 
    def speak(self): 
        return "Woof!" 
class Cat(Animal): 
    def speak(self): 
        return "Meow!" 
def make_animal_speak(animal): 
    print(animal.speak()) 
dog = Dog() 
cat = Cat()
make_animal_speak(dog)
make_animal_speak(cat)
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")

93)
# WAP to demonstrate Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
print("This Program Is Demonstrated By Kunal, ERP:- 0221BCA034")