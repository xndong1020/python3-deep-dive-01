def func1():
    "A single line docstring can use single quote"
    pass


# print(func1.__doc__)
# A single line docstring can use single quote


def func():
    """
    This is a multi-lines 
    docstring to example
    the usage of this function
    """
    pass


# print(func.__doc__)

"""
This is a multi-lines 
    docstring to example
    the usage of this function
"""


# help(func)

"""
Help on function func in module __main__:

func()
    This is a multi-lines 
    docstring to example
    the usage of this function
"""


# annotations
def func2(a: "a > 0", b: str) -> str:
    pass


# print(func2.__doc__) # None
# print(func2.__annotations__)
# {'a': 'a > 0', 'b': <class 'str'>, 'return': <class 'str'>}

# help(func2)

"""
Help on function func2 in module __main__:

func2(a: 'a > 0', b: str) -> str
    # annotations
"""

# annotations with multi-lines and default value
def func3(
    a: """
            multi-line annotation for parameter a
            """,
    *args: "additional parameters",
    b: int = 20,
    **kwargs: "additional keyword only params"
):
    pass
