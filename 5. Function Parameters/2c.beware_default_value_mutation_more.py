# def shopping(item, amount=1, store=[]):
#     store.append(f"Purchased {amount} of {item}")
#     return store


# store1 = shopping("Food")
# shopping("Paper", 2, store1)
# print(store1)  # ['Purchased 1 of Food', 'Purchased 2 of Paper']

# # we want to create a new store, but actually 2 stores object are refering to the same object
# store2 = shopping("milk", 5)
# print(store2)  # ['Purchased 1 of Food', 'Purchased 2 of Paper', 'Purchased 5 of milk']
# print(store1)  # ['Purchased 1 of Food', 'Purchased 2 of Paper', 'Purchased 5 of milk']
# print(store1 is store2)  # True

# """
# When this module is loaded, def was called, and the parameter store's default value
# is saved into cache, which is a mutation type.
# Later on whenever this function is called, the default value of store parameter is always
# pointing to the same object.
# """


def shopping(item, amount=1, store=None):
    store = store or []
    store.append(f"Purchased {amount} of {item}")
    return store


store1 = shopping("Food")
shopping("Paper", 2, store1)
print(store1)  # ['Purchased 1 of Food', 'Purchased 2 of Paper']

# we want to create a new store, but actually 2 stores object are refering to the same object
store2 = shopping("milk", 5)
print(store2)  # ['Purchased 5 of milk']
print(store1)  # ['Purchased 1 of Food', 'Purchased 2 of Paper']
print(store1 is store2)  # False
