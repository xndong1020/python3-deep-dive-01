from operator import attrgetter

s = "python"

partial_fn = attrgetter("upper")

print(partial_fn(s))  # <built-in method upper of str object at 0x10662d2f0>
print(partial_fn(s)())  #  PYTHON

print(attrgetter("upper")(s))  # <built-in method upper of str object at 0x10662d2f0>
print(attrgetter("upper")(s)())  #  'PYTHON'

from operator import methodcaller

print(methodcaller("upper")(s))  # meaning call 'upper()' method on s  -->  'PYTHON'
