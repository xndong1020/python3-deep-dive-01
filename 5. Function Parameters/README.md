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

(1) is not a tuple, it is 1, which is an integer

1, or (1,) is a tuple, because ',' defines a tuple

The only exception is when creating an empty tuple: () or tuple()

The simplest unpacking is:
```py
# unpacking list
a, b, c = [1, 2, 3]  ----> a=1, b=2, c=3

# unpacking tuple
a, b, c = 1, 2, 3    ----> a=1, b=2, c=3

# unpacking string
a, b, c = 'XYZ'      ----> a='X', b='Y', c='Z'
```
The unpacking into individual variables is based on the relatives positions of each element

##### simple application of unpacking: swapping values of 2 variables
```py
a = 10
b = 20

# using unpacking to swap value

a, b = b, a

#  this works because in Python, the entire RHS is evaluated first and complete, then assignments are made to LHS
# in our case, we create a tuple on the RHS with a, b initial values, i.e. (20, 10), then we unpack it to LHS, so a=20, b=10
```

##### We rarely use * to unpack in the LHS for Set and Dictionary
This is because when unpacking Set and Dictionary, * actual unpack the keys of Set and Dictionary, and Set and Dictionary are unordered types, they can be iterated, but there is  *NO guarantee* the order of the result will match your expectation.


#### 4. Extended Unpacking
##### The use case for *
We don't always want to unpack every single item in an iterable
We may, for example, want to unpack the first value, then unpack the remaining value into another variable
```py
# using slicing
l = [1, 2, 3, 4, 5, 6]

a = l[0]  # 1
b = l[1:]  # [2, 3, 4, 5, 6]
print(a)
print(b)

# using unpacking
c, d = l[0], l[1:]
print(c)  # 1
print(d)  # [2, 3, 4, 5, 6]


# using * operator
e, *f = l
print(e)  # 1
print(f)  # [2, 3, 4, 5, 6]
```

Note when use * operator to unpack, the remaining value will be unpack into a list, not matter what was the initial data type was:
```py
a, *b = [1, 2, 3, 4]  ---->  a=1, b=[2, 3, 4]
a, *b = (1, 2, 3, 4)  ---->  a=1, b=[2, 3, 4] # still a list
a, *b = "XYZ"         ---->  a="X", b=["Y", "Z"] # still a list
```

The following also works:
```py
a, b, *c = 1, 2, 3, 4, 5     ---->  a=1, b=2, c=[3, 4, 5]
a, b, *c, d = 1, 2, 3, 4, 5  ---->  a=1, b=2, c=[3, 4], d=5
```

The * operator can only be used *once* in the LHS an unpacking assignment, you cannot do `a, *b, *c = [1, 2, 3, 4, 5]`

##### Use * operator to merge ordered types
```py
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l = [*l1, *l2]   # [1, 2, 3, 4, 5, 6]
```

##### Use ** operator to merge unordered types
You can merge unordered types, but there is *no guarantee* for the order.

```py
d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}

d = {**d1, **d2, **d3} 

# {'p': 1, 'y': 2, 't': 3, 'h': 5, 'o': 6, 'n': 7}
```
note that the {'h': 5} from d3 **overrides** {'h': 4} from d2

##### nested unpacking
```py
# example 1:
l = [1, 2, [3, 4]]

# you can unpack it in 2 steps:
a, b, c = l  # a=1, b=2, c=[3,4]
d, e = c  # d=3, e=4

# this can be done in 1 step
a, b, (c, d) = l   # a=1, b=2, c=3, d=4

# example 2:
k, *l, (m, *n) = [1, 2, 3, 'python']
print(k) # 1
print(l) # [2, 3]
print(m) # p
print(n) # ['y', 't', 'h', 'o', 'n']
```




