#### 1. Docstrings and Annotations
##### Docstrings
We can document our functions (and modules, classes, etc) to achieve some documentations using docstrings **PEP 257**

If the **first line** in the function is a string (not a assignment, not a comment, just a string by itself), it will be interpreted as a `docstring`

Where is docstrings stored? In the function's __doc__ property
```py
def func1():
    "A single line docstring can use single quote"
    pass

print(func1.__doc__)
# A single line docstring can use single quote

def func():
    """
    This is a multi-lines 
    docstring to example
    the usage of this function
    """
    pass

print(func.__doc__)

"""
This is a multi-lines 
    docstring to example
    the usage of this function
"""
```

You can use help(<function_name>) to check the docstring for a function
```py
def func():
    """
    This is a multi-lines 
    docstring to example
    the usage of this function
    """
    pass

help(func)

"""
Help on function func in module __main__:

func()
    This is a multi-lines 
    docstring to example
    the usage of this function
"""
```

##### Function Annotations
Function annotations give us an additional way to document our functions. **PEP 3107**
The annotations are saved in function's __annotations__ property

The data type for annotation is dictionary
```py
{'a': 'a > 0', 'b': <class 'str'>, 'return': <class 'str'>}
```
keys are the parameter names
values are the annotations

```py
def func2(a: 'a > 0', b: str) -> str:
    pass

print(func2.__doc__) # None
print(func2.__annotations__)
# {'a': 'a > 0', 'b': <class 'str'>, 'return': <class 'str'>}
```

using help for annotations
```py
def func2(a: 'a > 0', b: str) -> str:
    pass

help(func2)

"""
Help on function func2 in module __main__:

func2(a: 'a > 0', b: str) -> str
    # annotations
"""
```

##### Annotations with multi-lines and default value
```py
def func3(
    a: """
            multi-line annotation for parameter a
            """,
    *args: "additional parameters",
    b: int = 20,
    **kwargs: "additional keyword only params"
):
    pass
```

##### Where does Python use docstrings and annotations?
Python doesn't really use them, it is mainly used by external tools and modules. 
Example: apps that generate documentation from your code. (Sphinx)

Docstrings and Annotations are entirely **optional** and do not "force" anything in our Python code



##### 2. Lambda Expressions
##### What are Lambda expressions?
Other than using "def" keyword, Lambda expressions are another way to create functions (anonymous functions)

```py
lambda [parameter list]: expression

parameter list is optional, you can pass zero parameters
: is required, even for zero parameters
expression must NOT have assignment, and must be single statement
```

Like functions defined with "def" keyword, when the module loaded, the lambda express is loaded, and returns a **function object**, but it is not called yet.

When the function is actually called, this function object is evaluated, and returns the expression

Some examples:
```py
lambda x: x**2
lambda x, y: x + y  # multiple parameters
lambda : "hello"  #  no parameter list
lambda word: word[::-1].upper()
```

##### limitation:
1. no assignments, you cannot do below
```py
lambda x: x = 5 #  wrong!!
```
2. no function annotations, you cannot do below
```py
lambda x:int : x**2  #  wrong!
```
3. Single logical line of code, line-continuation is ok, but still just **one** expression



#### 3. Lambdas and Sorting
##### Sorting integers
```py
nums = 8, 2, 9, 3, 1, 6

# sorted always returns a new list
sorted_list = sorted(nums)
print(sorted_list)  # [1, 2, 3, 6, 8, 9]
```

##### Sorting letters
When sorting letters, it is using its charCode, not necessarily in alphabetic order
```py
letters = ["c", "B", "D", "a"]

# when sorting letters, it is using its charCode, not necessarily in alphabetic order
sorted_letters = sorted(letters)
print(sorted_letters)  # ['B', 'D', 'a', 'c']

# to fix
sorted_letters_real = sorted(letters, key=lambda l: l.upper())
print(sorted_letters_real) #  ['a', 'B', 'c', 'D']
```

##### Sorting dictionary
You can't really sort a dictionary as it is an unordered type. But you can get sorted key in list from the dictionary
```py
items = {"food": 200, "paper": 300, "mile": 100}
# By default, it is sorted by dictionary keys, and you will get the list of sorted keys
sorted_items = sorted(items)
print(sorted_items)  #  ['food', 'mile', 'paper']

# you can specify to sort by value, but still you will get a list of sorted keys
sorted_items_amount = sorted(items, key=lambda key: items[key])
print(sorted_items_amount)  #  ['mile', 'food', 'paper']  ->  [100, 200, 300]
```

And once the keys are sorted, you can iterate through the dictionary by using sorted keys
```py
items = {"food": 200, "paper": 300, "mile": 100}

# you can specify to sort by value, but still you will get a list of sorted keys
sorted_items_amount = sorted(items, key=lambda key: items[key])
print(sorted_items_amount)  #  ['mile', 'food', 'paper']  ->  [100, 200, 300]


for key in sorted_items_amount:
    print(items[key])

"""
100
200
300
"""
```

##### How Python sort things if they have same value
```py
students = ["Cleese", "Idle", "Palin", "Chapman", "Gilliam", "Jones"]

students_sorted = sorted(students, key=lambda name: name[-1])
#  ['Cleese', 'Idle', 'Gilliam', 'Palin', 'Chapman', 'Jones']
print(students_sorted) 
```
Why 'Palin' appears before 'Chapman', but the last char of their name are both 'n'?
It is because Python is using "stable sort", which means if 2 things are the same, then Python will use the order originally specified in the list which you want to sort

In our case, the unsorted list, "students", 'Palin' appears before 'Chapman'


#### 4. Function Introspection
##### Functions are first-class Objects
1. Function has attributes
Some of the attributes are: __doc__  __annotation__
__name__   name of the function
__defaults__   tuple containing positional parameter defaults
__kwdefaults__ dictionary containing keyword-only parameter defaults

```py
def my_func(a, b=2, c=3, *, kw1, kw2=2):
    pass

my_func.__name__            my_func
my_func.__defaults__        (2, 3,)
my_func.__kwdefaults__      {'kw2': 2}   
```

__code__  <code object my_func at 0x00020EEF>

This __code__ object itself has various properties, which includes:
co_varnames:  parameter and local variables
co_argcount:  number of parameters
```py
def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

my_func.__code__.co_varnames    --->  ('a', 'b', 'args', 'kwargs', 'i')  # parameter names first, followed by local variable names

my_func.__code__.argcount       --->  2  # does NOT count *args and **kwargs
```

We can attach own attributes
```py
def my_func(a, b):
    pass

my_func.category = "math"
my_func.sub_category = "arithmetic"
```

We can check all the attributes attached on an object, by using dir() function
`dir()` is a built-in function that, given an object as an argument, will return a list of valid attributes for that object


##### The inspect Module
import inspect
1. ismethod(obj)  isfunction(obj)  isroutine(obj)   .... and many others

The difference between a function and a method?
Classes and objects have attributes - an object that is bound to (to the class or the object)
An attribute that is **callable**, is called a **method**

```py
# not bind to a class or class object
def my_func():
    pass

# bind to class
def MyClass:
    def func(self):
        pass

my_obj = MyClass()

isfunction(my_func)           # True
ismethod(my_func)             # False
isfunction(my_obj.my_func)    # False
ismethod(my_obj.func)         # True

# if it is either a method or a function, then isroutine returns True
isroutine(my_func)            # True
isroutine(my_obj.my_func)     # True
```

2. getsource(<function_name>), getmodule(<function_name>)
`getsource(<function_name>)` ---> returns a string containing our entire def statement, including annotations, docstrings, etc

`getmodule(<function_name>)` ----> returns the module containing the function
```
from inspect import getmodule

getmodule(my_func)    ->     <module  '__main__'>
getmodule(print)      ->     <module  'builtins'   (built-in)>
getmodule(math.sin)   ->     <module  'math'  (built-in)>
```

3. Callable Signatures
inspect.signatures(<function_name>)  -> returns a Signature instance, which has an attribute called parameters. Essentially it is a dictionary of parameter names(keys), and metadata about the parameters(values)
        keys   -> parameter name
        values -> object with attributes such as name, default, annotation, kind

kind is the kind of the parameter, POSITIONAL_OR_KEYWORD, VAR_POSITIONAL (*args), KEYWORD_ONLY, VAR_KEYWORD (**kwargs), POSITIONAL_ONLY


#### 5. callable
What are callable? 
Any object that can be called using `()` operator, callable always **return** a value, return value could be None.
We can use built-in function `callable` to check if an object is callable

##### Different Types of Callables
built-in functions          print, len, callable, etc
built-in methods            a_str.upper()   a_list.append(), etc
user-defined functions      created using `def` or `lambda` expressions
methods                     functions bound to an object
classes                     MyClass(x, y, z)
                              --> __new__(x, y, z)           -> for creating the new object
                              --> __init__(self, x, y, z)    -> for initialize properties
                              --> returns the object(reference)
class instances             if the class implements __call__ method
generators, coroutines, asynchronous generators

#### 6. Partial Functions
Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function. 

You can create partial functions in Python by using the partial function from the `functools` library. 
There are 3 ways that you can defined a partial function
```py
def my_func(a, b, c):
    print(a, b, c)

# way 1:
def partial_fn(b, c):
    return my_func(10, b, c)

partial_fn(20, 30)   ----> 10, 20, 30 # parameters passed to my_func

# way 2: lambda
lambda b, c: my_func(10, b, c) 
partial_fn(20, 30)   ----> 10, 20, 30 # parameters passed to my_func

# way3: functools library
from functools import partial
partial_fn = partial(my_func, 10)   # 10 will be passed as a positional argument, to 'a' param of my_func function
partial_fn(20, 39)   ----> 10, 20, 30 # parameters passed to my_func
```

A use case:
```py
from functools import partial

def pow(base, exponent):
    return base ** exponent

square = partial(pow, exponent=2)
cube   = partial(pow, exponent=3)

square(5)     ->  25
cube(5)       ->  125
cube(base=5)  ->  125
```

##### Beware!!
You can use variables when creating partials, but there arises a similar issue to argument default values. 

Example:
```py
def my_func(a, b, c):
    print(a, b, c)

a = 10
f = partial(my_func, a)  # the memory address of 10 is baked into the partial

f(20, 30)  --->  10, 20, 30

# now if you want to change the value for the partial function
a = 100
# and you are expecting f(20, 30)  ---> 100, 20, 30
# but still you will get f(20, 30)  --->  10, 20, 30, because the partial still points to the original object, which is 10

# Meanwhile, if a is mutable, then it's content can be changed
```

#### 6. The Operator Module
This module is a convenience module, you can always use your own functions and lambda expressions instead.

##### Arithmetic Functions
add(a, b)
mul(a, b)
power(a, b)
mod(a, b)
floordiv(a, b)  # floor division, floordiv(5, 2) -> 2. in Python the floor division operation is `//`
neg(a)

and many more...

##### Comparison and Boolean Operators
lt(a, b)     # check if 'a' less than 'b'
gt(a, b)   
eq(a, b)   
le(a, b)     # less or eq
ge(a, b)     # greater or eq
ne(a, b)     # not eq
is_(a, b)    
is_not(a, b)

and_(a, b)
or_(a, b)
not_(a, b)

##### Sequence/Mapping Operators
concat(s1, s2)
contains(s, val)     # if val exists in a sequence, equivalent to 'in' operator in Python
countOf(s, val)      # how many times does val occurs in a sequence
getitem(s, i)        # get item by index from a sequence, like s[i]
setitem(s, i, val)   # set s[i] = val
delitem(s, i)        # delete s[i]

##### Items Getters
The `itemgetter` function returns a callable
If compare the usage of getitem(s, i) and itemgetter(i)
```py
s = [1, 2, 3]
getitem(s, 0)  --->  1

from operator import itemgetter
fn = itemgetter(0)   # a partial function, to retrieve the first element from a sequence type 
fn(s)          --->  1
word = 'Python'
fn(word)       --->  'P' 
```
Real value of itemgetter function, is it can take more than 1 argument
```py
l = [1, 2, 3, 4, 5]
s = 'python'

partial_fn = itemgetter(1, 3, 4)

partial_fn(l)  ---> (2, 4, 5,)
partial_fn(s)  ---> ('y', 'h', 'o',)
```

##### Attribute Getters
The `attrgetter(item), attrgetter(*items)` funtion is similar to `itemgetter(item), itemgetter(*items)`, but is used to retrieve object attributes.
It takes object(s) as argument, and returns a callable

```py
# assume my_obj is an object with 3 properties
my_obj.a -> 10
my_obj.b -> 20
my_obj.c -> 30

partial_fn = attrgetter("a")
partial_fn(my_obj)   --> 10

partial_fn2 = attrgetter("a", "c")
partial_fn2(my_obj)  -->  (10, 30,)

# Can also call directly as a hoc:
attrgetter("a", "c")(my_obj)  --> (10, 30,)
```

And you can use it to call another callable
Consider the `str` class that provides the `upper()` method:
```py
s = 'python'       s.upper() --> 'PYTHON'

from operator import attrgetter

s = "python"

partial_fn = attrgetter("upper")

print(partial_fn(s))  # <built-in method upper of str object at 0x10662d2f0>
print(partial_fn(s)())  #  PYTHON

print(attrgetter("upper")(s))  # <built-in method upper of str object at 0x10662d2f0>
print(attrgetter("upper")(s)())  #  'PYTHON'
```

We have a similar function `methodcaller` from this module
```py
from operator import methodcaller
s = "python"
print(methodcaller("upper")(s))  # meaning call 'upper()' method on s  -->  'PYTHON'
```

