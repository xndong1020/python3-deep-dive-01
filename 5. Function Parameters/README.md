#### 1. Arguments vs Parameter
They have semantics difference only.

When you `define` a function
```py
def my_func(a, b):
    # code here
```
In this context, a and b are called parameters of my_func
`parameters` are within `Function Scope`

When we `call` a function
```py
x = 10
y = 'a'

my_func(x, y)
```
x and y are called the arguments of my_func
Also note that x and y are passed by `reference`
i.e. the memory address of x and y are passed
`arguments` are within `Module Scope`


#### 2. Positional and Keyword Arguments
Most common way of assigning argument to parameters: via the `order` in which they are passed
i.e. their position

```py
def my_func(a, b):
    # code ...

my_func(10, 20) -----> a = 10, b = 20
my_func(20, 10) -----> a = 20, b = 10
```

##### Default Value for a Parameter
A positional arguments can be made `optional` by specifying a `default value` for the corresponding parameter

```py
def my_func(a, b=100):
    # code ...

# You can call it normally
my_func(10, 20) -----> a = 10, b = 20

my_func(20) -----> a = 20, b = 100  # using default value
```
if a `positional parameter` is defined with a default value, every positional parameter after it must also be given a default value

```py
# you cannot have
def my_func(a, b=100, c):
    # code ...

# every positional parameter after it must also be given a default value
def my_func(a, b=100, c=50):
    # code ...
```

The problem with positional arguments is:
What if you want to specify the first and third arguments, but omit the second argument?

You can use keyword arguments

##### Keyword Arguments
`Keyword Arguments` also known as named arguments
```py
def my_func(a, b=100, c=50):
    # code ...

# to pass keyword argument, we need to use the parameter name
my_func(a=1, c=20)  -----> a = 1, b = 100, c = 2

my_func(1, c=2)     -----> a = 1, b = 100, c = 2 # in this case, a is positional argument
```

Positional arguments can, optionally, be specified by using the parameter name, whether or not the parameters have default value.

One of the benefits of using `keyword argument` is, the position of arguments are no longer important
```py
def my_func(a, b, c):
    # code ...

# without positional argument
my_func(1, 2, 3)             ----> a=1, b=2, c=3

# with positional argument
my_func(a=1, b=2, c=3)       ----> a=1, b=2, c=3

# is the same as
my_func(c=3, b=2, a=1)       ----> a=1, b=2, c=3
``` 

Note: Once you use a `keyword argument`, all arguments thereafter must be `named argument` to, you cannot do `my_func(c=1, 2, 3)` or `my_func(1, b=2, 3)`

```py
# wrong
my_func(c=1, 2, 3) 
# wrong
my_func(1, b=2, 3) 

# correct
my_func(1, b=2, c=3)
# correct
my_func(1, c=3, b=2) # position of keyword args does NOT matter
```

##### 3. Unpacking Iterables
A side note on Tuple
(1, 2, 3) is a tuple, but actually **what defines a tuple in Python is not (), but ,**
1, 2, 3 is also a tuple, the () are just used to make the tuple clearer


