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

