from datetime import datetime
from time import sleep


# def log(msg, *, dt=datetime.utcnow()):
#     # print(f"{msg} at {dt}")
#     print("{0} at {1}".format(dt, msg))


# log("test message")  #  2020-03-05 02:38:04.451668 at test message
# sleep(2)
# log("test message")  #  2020-03-05 02:38:04.451668 at test message
# sleep(2)
# log("test message")  #  2020-03-05 02:38:04.451668 at test message
# sleep(2)
# log("test message")  #  2020-03-05 02:38:04.451668 at test message
# sleep(2)
# log("test message")  #  2020-03-05 02:38:04.451668 at test message

"""
 The dt should NOT be the same, but why we have same output several times?
 This is because datetime.utcnow() is an object, it gets created, and saved into memory as default value of dt, and it is done when "def" run, not when the function is called, which means "dt" stays as the same object. So no matter how may times you call this function, dt default value stays the same. 
"""


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
