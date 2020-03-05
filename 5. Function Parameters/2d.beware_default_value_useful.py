# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         print(f"calculating factorial for {n}")
#         return n * factorial(n - 1)


# print(factorial(4))
# print(factorial(5))


"""
This function works. However every time it needs to start calculating
from scratch. If we need have a cache to memorize previous calculation 
it will have better performance
"""


def factorial(n, cache={}):
    if n <= 1:
        return 1

    #  if previous calculation result can be found in cache
    #  then no need to re-compute, just return
    if n in cache:
        return cache[n]

    # if no cache, then compute, and save result in cache
    print(f"calculating factorial for {n}")
    cache[n] = n * factorial(n - 1)
    return cache[n]


print(factorial(4))
print(factorial(5))


"""
calculating factorial for 4
calculating factorial for 3
calculating factorial for 2
24
calculating factorial for 5
120

The reason why 2 function calls are sharing the same cache, is
because when this module is loaded, def keyword saves function,
and the cache's default value is saved 

So for every function call, they are sharing the same cache default value
"""
