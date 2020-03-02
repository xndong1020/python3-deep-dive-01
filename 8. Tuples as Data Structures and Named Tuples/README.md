#### Tuples as Data Structure

##### 1. Immutability of Tuples
* element cannot be added or removed
* the order of elements cannot be changed
* 'tuple' object does not support item assignment

```py
new_york = ('New York', 'USA', '8,500,000')

print(type(new_york)) # <class 'tuple'>

new_york[0] = 'Huston'  # TypeError: 'tuple' object does not support item assignment
```
* works well for representing data structures, think of a tuple as a data record where the position of the data has meaning. 


##### 2. Extracting data from Tuples
* using unpacking
```py
# actually tuple doesn't need brackets
new_york = "New York", "USA", "8,500,000"
city, country, population = new_york
print(city)  # New York
print(country)  # USA
print(population)  # 8,500,000
```

##### 3. Dummy Variables
If you are only interested in a subset of the data fields in a tuple, not all of them
Below skip `'country'` field

```py
new_york = "New York", "USA", "8,500,000"
city, _, population = new_york
```
_ is actually a legal variable name, nothing special about it, but by convention, we use the underscore to indicate this is a variable we don't care about

if we need to skip multiple fields:
```py
record = ("DJIA", 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.72)
# symbol, year, month, day, open, high, low, close = record

# if you want to skip open, high and low
symbol, year, month, day, *_, close = record

print(symbol, year, month, day, close)  # DJIA 2018 1 19 26071.72
print("dummy variables", *_)  # dummy variables 25987.35 26071.72 25942.83
```

