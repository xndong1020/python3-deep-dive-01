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

#### 5. *args
Recall `a, b, *c = 10, 20, 'a', 'b'` --> `a=10 b=10 c=['a', 'b']`

Something similar happens when **positional arguments** are passed to a function:

```py
del func(a, b, *c):
    # code

func(10, 20, 'a', 'b')  --> a=10 b=20 c=('a', 'b',)
```
Note: the difference is ***args is a tuple**, **not a list**

It is customary (but not required) to mane it to *args

###### *args exhausts positional arguments
You cannot add more positional arguments after *args
```py
def func(a, b, *args, d):
    # code

# you cannot use positional arguments after *args, because *args exhausts positional arguments
func(10, 20, 'a', 'b', 'c') # this will not work
# because *args exhausts positional arguments, so d has to be a kwargs
func(10, 20, 'a', 'b', d='c')
```

##### Unpacking arguments
```py
def func(a, b, c):
    # code

lst = [10, 20, 30]

func(lst) # this will NOT work, func is expecting 3 positional arguments, but you just passed in 1 argument which is lst

# You can unpack the list first and then pass it to the function
func(*lst)
```

##### Why use *args?
The main reason is, with *args you can pass any number of positional argument to a function

```py
# without *args, below function only accepts 3 arguments, no more, no less
def my_func(a, b, c):
    # code

# with *args, below function can accept any number of arguments
def avg(*args):
    count = len(*args)
    total = sum(*args)
     # if count is 0, return 0, otherwise return total/count
    return count and total/count
```

Note the difference between `def avg(*args)` and `def avg(a, *args)`,
`def avg(*args)` accepts 0 or more arguments, whereas `def avg(a, *args)` accepts 1 or more arguments, because a is a required positional argument


#### 6. keyword arguments
Recall that positional parameters can, optionally be passed as named (keyword) arguments
```py
def func(a, b, c):
    # code

# you can pass in positional arguments
func(1, 2, 3)
# or named arguments
func(c=3, a=1, b=2)
```

##### Mandatory Keyword Arguments
We can make **keyword arguments** mandatory
To do so, we create parameters after the positional parameters have been exhausted.

```py
def func(a, b, *args, d):
    # code

# In this case, *args efficiently exhausted all positional arguments,  and 'd' must be passed as keyword (named) argument

# below 2 cases are valid
func(1, 2, 'x', 'y', d=100) --> a=1 b=2 args=('x', 'y') d=100
func(1, 2, d=100)           --> a=1 b=2 args=() d=100

# but this is NOT valid, as 'd' is a mandatory keyword parameter
func(1, 2)  # missing mandatory keyword parameter
```

We can even omit any mandatory positional arguments:
```py
def func(*args, d):
    # code

func(1, 2, 3, d=100)  ---> args=(1, 2, 3), d=100
func(d=100)           ---> args=(), d=100
```

In face, we can force **no positional arguments** at all:
```py
# * indicates the "end" of positional arguments
def func(*, d):
    # code

# below example throw exception, because no mandatory positional argument before "*", and "*" means end of positional arguments
func(1, 2, 3, d=100)  # exception
function(d=100)       # correct, d=100
```

##### Put it together
```py
def func(a, b=1, *args, d, e=True):
    # code

def func(a, b=1, *, d, e=True):
     # code

# In these 2 examples:
a is mandatory positional argument, 
b is a optional argument, default value is 1. 
args: catch-all for any (optional) additional positional arguments
*: no additional positional arguments allowed
d: mandatory keyword argument
e: optional keyword argument, default to True
```

##### 7. **kwargs
***args** is used to scoop up variable amount of remaining positional arguments

**kwargs is used to scoop up variable amount of remaining keyword arguments

**kwargs can be specified even if the positional arguments have NOT been exhausted (unlike keyword-only arguments)

```py
def func(*, d, **kwargs):
    # code

func(d=1, a=2, b=3)   ---->  d=1 kwargs={"a": 2, "b": 3}
func(d=1)             ---->  d=1 kwargs={}
```

```py
def func(**kwargs):
    # code

func(a=1, b=2, c=3)  ----> kwargs={"a": 1, "b": 2, "c": 3}
func( )              ----> kwargs={}
```

```py
def func(*args, **kwargs):
    # code

func(1, 2, a=10, b=20) ----> args=(1, 2,)  kwargs={"a": 10, "b": 20}
```

You cannot put positional arguments after **kwargs
```py
def func(*args, **kwargs):
    # code

func(1, 2, x=100, y=200, 12)  # wrong. You cannot put positional arguments after **kwargs
```

You can use * to signal there is no more positional arguments
```py
def func(a, b, *, d, **kwargs):
    # code

func(1, 2, d=20, x=100, y=200) ---> a=1 b=2 d=20, kwargs={"x": 100, "y": 200}
```

##### an complex example
```py
print(*objects, sep='', end='\n', file=sys.stdout, flush=False)

*objects accept variable amount of positional arguments
sep is an optional keyword argument, default value is ''
end is an optional keyword argument, default value is '\n'
file is an optional keyword argument, default value is sys.stdout
flush is an optional keyword argument, default value is False
```


#### 9. Parameter Defaults - Beware!
What happens at runtime:
1. when a module is loaded, all code in the module is executed immediately

Example Module Code:
```py
a = 10      -->  the integer object 10 is created, and references it

def func(a): 
    # code
     --> 'def' keyword is seen, the function object is created, and func references it
```

2. with default values:
```py
def func(a=10):  
    # code
    --> 'def' keyword is seen, the function object is created, and func references it
    --> the integer object 10 is evaluated/created, and is assigned as the default for a
```

This will potentially cause some problem.
Case 1:
```py
from datetime import datetime
from time import sleep


def log(msg, *, dt=datetime.utcnow()):
    # print(f"{msg} at {dt}")
    print("{0} at {1}".format(dt, msg))


log("test message")  #  2020-03-05 02:38:04.451668 at test message
sleep(2)
log("test message")  #  2020-03-05 02:38:04.451668 at test message
sleep(2)
log("test message")  #  2020-03-05 02:38:04.451668 at test message
sleep(2)
log("test message")  #  2020-03-05 02:38:04.451668 at test message
sleep(2)
log("test message")  #  2020-03-05 02:38:04.451668 at test message

```

 The dt should NOT be the same, but why we have same output several times?
 This is because datetime.utcnow() is an object, it gets created, and saved into memory as default value of dt, and it is done when "def" run, not when the function is called, which means "dt" stays as the same object. So no matter how may times you call this function, dt default value stays the same.


 Solution pattern:
 ```py
 # Now the dt is still optional. If user did NOT pass in value for dt, it's default value is None, and in the code will call datetime.utcnow(), and datetime.utcnow() is not cached.
 def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print("{0} at {1}".format(dt, msg))


log("test message")  #  2020-03-05 02:45:14.134404 at test message
sleep(2)
log("test message")  #  2020-03-05 02:45:16.136592 at test message
sleep(2)
log("test message")  #  2020-03-05 02:45:18.136868 at test message
sleep(2)
log("test message")  #  2020-03-05 02:45:20.140748 at test message
sleep(2)
log("test message")  #  2020-03-05 02:45:20.140748 at test message
 ```

```py
list = [1, 2, 3]


def func(list=list):
    print(list)


func()  # [1, 2, 3]

list.append(4)

func()  # [1, 2, 3, 4], which means default value changed!!
```
Ideally if user not specify list keyword argument, if should always print out the same value, which is [1,2,3]
However if someone changed the value of list, the output will change, it is not what we want

Solution:
```py
list = (1, 2, 3)


def func(list=list):
    print(list)


func()  # [1, 2, 3]

list.append(4)  
# YOU CAN'T change a immutable tuple, so the default value of list is always the same
```