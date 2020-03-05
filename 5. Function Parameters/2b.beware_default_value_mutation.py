# we need to be careful of using Mutation types as default value
# list = [1, 2, 3]


# def func(list=list):
#     print(list)


# func()  # [1, 2, 3]

# list.append(4)

# func()  # [1, 2, 3, 4], which means default value changed!!

"""
Ideally if user not specify list keyword argument, if should always print out the same value, which is [1,2,3]
However if someone changed the value of list, the output will change, it is not what we want
"""

list = (1, 2, 3)


def func(list=list):
    print(list)


func()  # [1, 2, 3]

list.append(4)
# YOU CAN'T change a immutable tuple, so the default value of list is always the same
