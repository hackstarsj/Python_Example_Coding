# What is Python? What are its key features?
# Explanation: Python is a high-level, interpreted, and dynamically-typed programming language. It is known for its easy-to-read syntax and versatility. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

# Simple Python code to demonstrate Python's syntax
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))  # Output: Hello, World!


# 2. What are the different data types in Python?
# Explanation: Python has a variety of built-in data types. These include:

# Numeric Types:
# int: Integer values, e.g., 5
# float: Floating-point numbers, e.g., 3.14
# complex: Complex numbers, e.g., 2+3j

# Text Type:
# str: String, e.g., "Hello"

# Sequence Types:
# list: Ordered, mutable collection, e.g., [1, 2, 3]
# tuple: Ordered, immutable collection, e.g., (1, 2, 3)
# range: Sequence of numbers, e.g., range(5) generates numbers from 0 to 4.

# Mapping Type:
# dict: Unordered collection of key-value pairs, e.g., {"key": "value"}

# Set Types:
# set: Unordered collection of unique elements, e.g., {1, 2, 3}

# Boolean Type:
# bool: Boolean values True or False.
# Binary Types:
# bytes: Immutable byte sequences, e.g., b'hello'
# bytearray: Mutable byte sequences.
# memoryview: Memory view objects.

# Different data types in Python
a = 5         # int
b = 3.14      # float
c = 2 + 3j    # complex
d = "Hello"   # string
e = [1, 2, 3] # list
f = (1, 2, 3) # tuple
g = {1, 2, 3} # set
h = {'a': 1, 'b': 2} # dict

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'complex'>
print(type(d))  # Output: <class 'str'>
print(type(e))  # Output: <class 'list'>
print(type(f))  # Output: <class 'tuple'>
print(type(g))  # Output: <class 'set'>
print(type(h))  # Output: <class 'dict'>


# 3. What is the difference between Python 2.x and 3.x?
# Explanation: Python 2.x and Python 3.x are different versions of Python, and Python 3.x was introduced to address and improve some features in Python 2.x. The key differences are:


# Print Statement:
# In Python 2.x, the print statement is used without parentheses, e.g., print "Hello".
# In Python 3.x, the print function is used with parentheses, e.g., print("Hello").

# Division:
# In Python 2.x, the division of two integers results in an integer value, e.g., 5 / 2 = 2.
# In Python 3.x, the division of two integers results in a float value, e.g., 5 / 2 = 2.5.

# Unicode Support:
# Python 2.x uses ASCII encoding by default, and Unicode strings are specified with a "u" prefix.
# Python 3.x uses Unicode encoding by default, and all strings are Unicode strings.

# xrange vs range:
# In Python 2.x, xrange() generates numbers on demand and is more memory-efficient for large ranges.
# In Python 3.x, range() behaves like Python 2.x's xrange() and generates numbers on demand.

# Error Handling:
# In Python 2.x, the syntax for handling exceptions is "except Exception, e:".
# In Python 3.x, the syntax for handling exceptions is "except Exception as e:".

# Input Function:
# In Python 2.x, the input() function evaluates the input as Python code.
# In Python 3.x, the input() function returns the input as a string.

# Key differences between Python 2.x and 3.x
# Python 2.x
# print "Hello"  # Output: Hello
# print 5 / 2    # Output: 2
# print u"Hello" # Unicode string
# xrange(5)      # Generates numbers on demand
# except Exception, e: # Exception handling syntax
# input()        # Evaluates input as Python code

# Python 3.x
print("Hello")  # Output: Hello
print(5 / 2)    # Output: 2.5
print("Hello")  # Unicode string
range(5)        # Generates numbers on demand
try:
    raise Exception("Error")
except Exception as e:
    print(e)    # Exception handling syntax
input()         # Returns input as a string



#4. How is memory managed in Python?
# Explanation: Memory management in Python is handled by the Python memory manager. Key points include:
# Reference Counting: Python uses reference counting to track objects. When the reference count of an object drops to zero, the memory is released.
# Garbage Collection: Python has a garbage collector that handles the deallocation of objects with circular references.
# Memory Allocation: Python uses private heaps to store objects. Python’s built-in memory manager ensures efficient allocation and deallocation.
# Memory Optimization: Python uses techniques like memory pooling, small-object optimization, and copy-on-write to optimize memory usage.

# Memory management in Python
import sys
# Get the size of an object in bytes
object_size = sys.getsizeof(a)
print(f"Size of object 'a': {object_size} bytes")

# Get the total memory used by the Python process
process_memory = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c) + sys.getsizeof(d)
print(f"Total memory used by the Python process: {process_memory} bytes")


# 5. Explain the difference between lists and tuples.
# Explanation: Lists and tuples are both sequence data types in Python, but they have key differences:
# Mutability: Lists are mutable, meaning their elements can be changed after creation. Tuples are immutable, meaning their elements cannot be changed after creation.
# Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses ().
# Performance: Tuples are generally faster than lists for iteration and indexing, as they are immutable and require less memory.
# Use Cases: Lists are used when the order of elements needs to be changed or modified. Tuples are used when the order of elements should not be changed or for fixed-size collections.

# Difference between lists and tuples
my_list = [1, 2, 3]  # List
my_tuple = (1, 2, 3) # Tuple

# Mutability
my_list[0] = 4  # Valid for lists
# my_tuple[0] = 4 # Invalid for tuples

# Syntax
print(my_list)  # Output: [4, 2, 3]
print(my_tuple) # Output: (1, 2, 3)

# Performance
import timeit
list_time = timeit.timeit('for i in my_list: pass', globals=globals(), number=1000000)
tuple_time = timeit.timeit('for i in my_tuple: pass', globals=globals(), number=1000000)

print(f"List iteration time: {list_time}")
print(f"Tuple iteration time: {tuple_time}")

# Write Complexity
# List
# Append: O(1)
# Insert: O(n)
# Delete: O(n)

# Tuple
# Append: O(n)
# Insert: O(n)
# Delete: O(n)

# 6. How do you create a function in Python?
# Explanation: Functions in Python are defined using the def keyword followed by the function name and parameters. Key points include:
# Function Name: The name of the function should be descriptive and follow Python naming conventions.
# Parameters: Functions can take zero or more parameters, which are specified within parentheses.
# Return Value: Functions can return a value using the return keyword. If no return value is specified, the function returns None.
# Docstring: It is good practice to include a docstring that describes the purpose of the function.
# Function Call: Functions are called by using the function name followed by parentheses and any required arguments.

# Creating a function in Python
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8

# 6A. What is a lambda function in Python?
# Explanation: Lambda functions, also known as anonymous functions, are small, inline functions defined using the lambda keyword. Key points include:
# Syntax: Lambda functions are defined using the lambda keyword followed by parameters and an expression.
# Single Expression: Lambda functions can only contain a single expression, and the result of the expression is returned.
# No Return Statement: Lambda functions do not require a return statement, as the expression result is automatically returned.
# Use Cases: Lambda functions are often used for short, simple operations where defining a full function is unnecessary.

# Lambda function in Python
add = lambda a, b: a + b
result = add(5, 3)
print(result)  # Output: 8


# 7. **What are *args and kwargs in Python?
# Explanation: *args and **kwargs are used in Python to handle variable-length arguments in functions. Key points include:
# *args: *args is used to pass a variable number of non-keyword arguments to a function. The arguments are passed as a tuple.
# **kwargs: **kwargs is used to pass a variable number of keyword arguments to a function. The arguments are passed as a dictionary.
# Naming Convention: *args and **kwargs are naming conventions, and the * and ** symbols are important.
# Order of Parameters: *args must come before **kwargs in function definitions.
# Use Cases: *args and **kwargs are commonly used when the number of arguments to a function is not known in advance.

# Using *args and **kwargs in Python
def example_function(*args, **kwargs):
    print("Non-keyword arguments:")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(1, 2, 3, name="Alice", age=30)

# Output:
# Non-keyword arguments:
# 1
# 2
# 3

# Keyword arguments:
# name: Alice
# age: 30


# 9. How is Python an interpreted language?
# Explanation: Python is an interpreted language, which means the code is executed line by line by an interpreter. Unlike compiled languages like C or C++, Python does not need to be compiled before execution, which makes it easy to test and debug.
# Advantages of Interpretation: Interpreted languages like Python offer advantages such as portability, ease of use, and dynamic typing.
# Disadvantages of Interpretation: Interpreted languages may have slower execution speeds compared to compiled languages, as the code is not pre-compiled.
# Python Interpreter: The Python interpreter reads the source code, compiles it into bytecode, and then executes the bytecode. This process is transparent to the user and allows for interactive development.

# Python as an interpreted language
# Python code is executed line by line by the interpreter
# No separate compilation step is required
# Easy to test and debug code

# 10. What are Python decorators?
# Explanation: A decorator is a higher-order function that takes another function as an argument and extends or alters its behavior without explicitly modifying it. Decorators are often used for logging, authentication, etc.

# Syntax: Decorators are defined using the @decorator_name syntax above the function definition.

# Use Cases: Decorators are commonly used to add functionality to existing functions without modifying their code.

# Python decorators
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Before function execution
# Hello!
# After function execution

# 11. What is the difference between shallow copy and deep copy?

# Explanation: Shallow copy and deep copy are two ways to create copies of objects in Python. Key differences include:

# Shallow Copy: A shallow copy creates a new object but does not create copies of nested objects. Changes to nested objects in the copy will affect the original object and vice versa.
# Deep Copy: A deep copy creates a new object and recursively creates copies of nested objects. Changes to nested objects in the copy will not affect the original object and vice versa.

# Use Cases: Shallow copies are used when you want to create a new object with the same top-level structure. Deep copies are used when you want to create a new object with copies of all nested objects.

# Difference between shallow copy and deep copy
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)

# Modify the nested list in the shallow copy
shallow_copy[0][0] = 100

print(original_list)  # Output: [[100, 2, 3], [4, 5, 6]]

deep_copy = copy.deepcopy(original_list)

# Modify the nested list in the deep copy
deep_copy[0][1] = 200

print(original_list)  # Output: [[100, 2, 3], [4, 5, 6]]

#Example of shallow copy and deep copy in Python in Dictionary


# Shallow copy and deep copy in Python
import copy

original_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
shallow_copy = copy.copy(original_dict)

# Modify the nested list in the shallow copy
shallow_copy['a'][0] = 100

print(original_dict)  # Output: {'a': [100, 2, 3], 'b': [4, 5, 6]}

deep_copy = copy.deepcopy(original_dict)

# Modify the nested list in the deep copy
deep_copy['b'][1] = 200

print(original_dict)  # Output: {'a': [100, 2, 3], 'b': [4, 5, 6]}


# 12. Explain Python's list comprehension.
# Explanation: List comprehension is a concise way to create lists in Python. Key points include:

# Syntax: List comprehension is defined using square brackets [] with an expression and optional conditions.
# Readability: List comprehension is often more readable and concise than traditional loops.
# Performance: List comprehension can be more efficient than traditional loops for creating lists.
# Use Cases: List comprehension is commonly used to create new lists by transforming or filtering existing lists.

# Python list comprehension
numbers = [1, 2, 3, 4, 5]

# Traditional loop
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# List comprehension
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#if else in list comprehension
# List comprehension with conditional
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4]

#filtering with list comprehension
# List comprehension with conditional
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)  # Output: [2, 4]

#if else in list comprehension
# List comprehension with conditional
even_numbers = [num if num % 2 == 0 else "Odd" for num in numbers]
print(even_numbers)  # Output: ['Odd', 2, 'Odd', 4, 'Odd']


# 13. What are Python generators?

# Explanation: Generators in Python are functions that can be paused and resumed, yielding multiple values over time. Key points include:

# Yield Statement: Generators use the yield statement to return values one at a time. The function state is saved between yields.
# Lazy Evaluation: Generators use lazy evaluation, generating values on-demand rather than all at once.
# Memory Efficiency: Generators are memory-efficient, as they do not store all values in memory at once.

# Use Cases: Generators are commonly used for iterating over large datasets, generating infinite sequences, and implementing custom iterators.

# Python generators
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# Factorial using generator
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


for value in factorial(5):
    print(value)

# Output:
# 1
# 2
# 6
# 24
# 120

#Fabonacci series using generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for value in fibonacci(20):
    print(value)


# 14. What is the difference between is and == in Python?

# Explanation: In Python, the is operator is used to compare object identity, while the == operator is used to compare object equality. Key differences include:

# is: The is operator compares the memory address of two objects to check if they are the same object.
# ==: The == operator compares the values of two objects to check if they are equal.
# Use Cases: Use is to check if two variables refer to the same object. Use == to check if two variables have the same value.

# Difference between is and ==
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True (a and b refer to the same object)
print(a is c)  # Output: False (a and c refer to different objects)

print(a == b)  # Output: True (a and b have the same value)
print(a == c)  # Output: True (a and c have the same value)

# 15. What is the purpose of the self keyword in Python?

# Explanation: In Python, the self keyword is used to refer to the current instance of a class. Key points

# Instance Method: The self keyword is used as the first parameter in instance methods to refer to the current instance.
# Accessing Attributes: The self keyword is used to access instance attributes and methods within a class.
# Naming Convention: While self is the conventional name, any name can be used for the first parameter in instance methods.
# Use Cases: The self keyword is used to differentiate instance attributes and methods from local variables and function parameters.

# Purpose of the self keyword in Python
class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

obj = MyClass(5)
obj.print_value()  # Output: 5

# Without using self keyword
class MyClass2:
    def __init__(this, value):
        this.value = value

    def print_value(this):
        print(this.value)

obj = MyClass2(51)
obj.print_value()  # Output: 5


# 16. What is inheritance in Python?

# Explanation: Inheritance is a key feature of object-oriented programming in Python. Key points include:

# Base Class: The class whose attributes and methods are inherited is called the base class or parent class.
# Derived Class: The class that inherits attributes and methods from the base class is called the derived class or child class.
# Code Reusability: Inheritance allows code reuse by creating a new class that extends the functionality of an existing class.
# Method Overriding: Derived classes can override methods of the base class to provide specialized behavior.
# Use Cases: Inheritance is used to create a hierarchy of classes with shared attributes and methods.

# Inheritance in Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speaks")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

animal = Animal("Animal")
animal.speak()  # Output: Animal speaks

dog = Dog("Buddy", "Labrador")
dog.speak()  # Output: Buddy barks

# 17. What is method overloading and method overriding in Python?

# Explanation: Method overloading and method overriding are two ways to achieve polymorphism in Python. Key differences include:

# Method Overloading: Method overloading allows a class to define multiple methods with the same name but different parameters. Python does not support method overloading by default.
# Method Overriding: Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. The method
# in the subclass overrides the method in the superclass.
# Use Cases: Method overloading is used to define multiple methods with the same name but different parameters. Method overriding is used to provide a specialized implementation of a method in a subclass.

# Method overloading and method overriding in Python
class MyClass:
    def my_method(self, a=None, b=None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print("No arguments")

class MySubClass(MyClass):
    def my_method(self, a, b):
        print(a * b)

obj = MyClass()
obj.my_method(5)    # Output: 5

sub_obj = MySubClass()
sub_obj.my_method(5, 3)  # Output: 15

# Implementing method overloading in Python
class MyClass:
    def my_method(self, *args):
        if len(args) == 1:
            print(args[0])
        elif len(args) == 2:
            print(args[0] + args[1])

obj = MyClass()
obj.my_method(5)    # Output: 5
obj.my_method(5, 3)  # Output: 8

# Design Patterns in Python 
# A. What is the Singleton design pattern in Python?
# Explanation: The Singleton design pattern ensures that a class has only one instance and provides a global point of access to that instance. Key points include:

# Single Instance: The Singleton pattern restricts the instantiation of a class to a single
# instance.
# Global Access: The Singleton pattern provides a global point of access to the single instance.
# Implementation: The Singleton pattern is implemented by defining a static method to create or return the single instance.
# Use Cases: The Singleton pattern is used when only one instance of a class is needed throughout the application.

# __new__ method: The __new__ method is used to create a new instance of a class. In the Singleton pattern, the __new__ method is overridden to ensure that only one instance is created.

# Singleton design pattern in Python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        print("Instance created")

    def __del__(self):
        print("Instance deleted")

    def print_message(self):
        print("Hello, Singleton!")

# Creating instances of Singleton    
obj1 = Singleton()
obj1.print_message()


# B. What is the Factory design pattern in Python?
# Explanation: The Factory design pattern is a creational pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. Key points include:

# Interface: The Factory pattern defines an interface for creating objects but lets subclasses decide which class to instantiate.
# Decoupling: The Factory pattern decouples the client code from the object creation logic, making it easier to add new types of objects.
# Implementation: The Factory pattern is implemented by defining a factory method that creates objects based on input parameters.
# Use Cases: The Factory pattern is used when a class cannot anticipate the class of objects it must create.

# Factory design pattern in Python
class Shape:
    def draw(self):
        pass
    
class Circle(Shape):
    def draw(self):
        print("Circle drawn")

class Rectangle(Shape):
    def draw(self):
        print("Rectangle drawn")

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Invalid shape type")
        
# Creating objects using the factory
circle = ShapeFactory.create_shape("circle")
circle.draw()  # Output: Circle drawn

rectangle = ShapeFactory.create_shape("rectangle")
rectangle.draw()  # Output: Rectangle drawn

