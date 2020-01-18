## Section 02: A Quick Refresher - Basic Review
#### 5. The Python Type Hierarchy
1. Numbers: Integral Numbers (Integers, Boolean), Non-Integral (Floats, Complex, Decimals, Fractions)
```python
from fractions import Fraction 
   
print(Fraction(11, 35), type(Fraction(11, 35)))

print(Fraction(10, 18), type(Fraction(10, 18)))
  
print(Fraction(), type(Fraction(10, 18))) 
```

Output:
```
11/35 <class 'fractions.Fraction'>
5/9 <class 'fractions.Fraction'>
0 <class 'fractions.Fraction'>
```

2. Collections: 
```
|--Sequences
 ------Mutable
       -----Lists
 ------Immutable
       -----Tuples (can be seen as immutable version of Lists)
       -----Strings
|--Sets
-------Mutable
       ----- Sets
-------Immutable
       ----- Frozen Sets
|--Mappings
-------------Dictionaries
```

3. Callable
Anything that you can invoke
```python
User-Defined Functions
Built-in Functions (e.g. len(), open())
Built-in Methods (e.g. my_list.append(x))
Generators
Classes
Instance Methods
Class Instances(__call__())
```

4. Singletons
```
None
NotImplemented
Ellipsis(...)
```


#### 06. Multi-Line Statements and Strings
Python supports multi-line statement
```
Python program 
    --------> physical lines of code    when you hit enter key and goes to the next lien in your code editor, it ends with a physical newline character
        ---------> logical lines of code, python compiler combines a few lines, and makes a logical line of code,  it ends with a logical NEWLINE token
           ----------> tokenized, python interpreter will then figure out what you are trying to do and execute it
```

physical newline vs logical newline
```
We use physical newlines for code readability, but python interpreter doesn't need that. Sometimes, physical newlines are ignored in order to combine multiple physical lines into a single logical line of code
Logical line terminated by a logical NEWLINE token
```

implicit multiple line
```python
a = [ 1, 2, 3]

equals

a = [1,
     2,
     3]

equals

a = [1, # some comment
     2, # more comment
     3 #another comment]
```

explicit multiple line
1. use `\` character, comment cannot be part of a statement
```python
if a \
   and b \
   and c:
```

2. use multi-line string literals
```python
''' This is 
a multi-line string '''

equals
""" This is 
a multi-line string """
```
Caveat: Be aware that non-visible characters such as newlines, tabs, etc. are actually part of the string - basically anything you type.

```python
a = '''this 
     is a string
        that is created over multiple lines'''
```
it actually contains \n and tabs, which you can't see. 

You can use escaped characters (e.g. \n, \t), use string formatting ,etc.



#### 09. Functions
Python is a dynamic typing language. If you put type annotation in your function parameters list, it just a documentation thing
```py
def func_02(a: int, b: int):
    return a * b

func_02('a', 3) # will output 'aaa'
```

```py
def func_03():
    func_04()

def func_04():
    print('running func_04')

func_03() # this will work, at evaluation time, func_04 DOES exist


def func_03():
    func_04()

func_03() # this will NOT work, at evaluation time, func_04 DOES NOT exist

def func_04():
    print('running func_04')
```

#### 13. Classes
define a class using `class` keyword

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

```

the `__init()__` function will be run once the object **has been created**, it runs after the `new object` phrase

```py
r1 = Rectangle(10, 20)

print(str(r1)) # <__main__.Rectangle object at 0x7f2c04e1ef98>

```

Implement `__repr()__` for any class you implement. This should be second nature. Implement `__str()__` if you think it would be useful to have a string version which errs on the side of readability.

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return 'Rectangle str: width={0}, height={1}'.format(self.width, self.height)

    def __prep__(self):
        return 'Rectangle prep: width={0}, height={1}'.format(self.width, self.height)
```

```py
r1 = Rectangle(10, 20)

# when you print r1, it will use __str__
print(str(r1))  # Rectangle str: width=10, height=20
print(r1) # Rectangle str: width=10, height=20
```

equality and `__eq()__` method
```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return (self.width * self.height) == (other.width * other.height)
         


r1 = Rectangle(10, 20)
r2 = Rectangle(20, 10)

print(r1 is r2) # False, they have different address, hence they are different object
print(r1 == r2) # True, use __eq__ method to define how to compare
print(r1 == 200) # Error. int object has no attribute `width`
```

Change our code to:
```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
           return (self.width * self.height) == (other.width * other.height)
        else:
           return self.width * self.height == other
         


r1 = Rectangle(10, 20)
r2= Rectangle(20, 10)

print(r1 is r2) # False, they have different address, hence they are different object
print(r1 == r2) # True, use __eq__ method to define how to compare
print(r1 == 200) # True
```

**Do we use getters and setters in Python?**
The answer is `yes and no`. Unlike Java, which you always have to write getters and setters. In Python, unless you know that you have specific reason to implement a specific getter or setter that has extra logic, you don't implement them.

In before code, only if we need to make sure the width is positive, we then use getter and setter, in pythonic way.

```py
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property # getter method to read value from field _width
    def width(self):
        return self._width

    @width.setter # getter method to encapsulate field _width
    def width(self, value):
        if value <= 0:
           raise ValueError('Width must be positive')
        else:
           self._width = value

    def area(self):
        return self.width * self.height
         


r1 = Rectangle(10, 20)
r1.width = 2000 # setter
print(r1.width)  # getter, result is 2000
```
But now if we do this:
```py
r1 = Rectangle(-100, 20)
```
It will not raise error, because we don't have protect logic in __init()__ method

we can do this:
```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property # getter method to read value from field _width
    def width(self):
        return self._width

    @width.setter # getter method to encapsulate field _width
    def width(self, value):
        if value <= 0:
           raise ValueError('Width must be positive')
        else:
           self._width = value

    def area(self):
        return self.width * self.height
         


r1 = Rectangle(-100, 20)
```

This code this use getter in `__init()__` method, and python will create _width for you 

