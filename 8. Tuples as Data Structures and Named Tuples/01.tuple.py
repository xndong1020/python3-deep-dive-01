new_york = ("New York", "USA", "8,500,000")
print(type(new_york))  # <class 'tuple'>

# new_york[0] = 'Huston'  # TypeError: 'tuple' object does not support item assignment

# actually tuple doesn't need brackets
new_york = "New York", "USA", "8,500,000"
city, country, population = new_york
print(city)  # New York
print(country)  # USA
print(population)  # 8,500,000


# dummy variables

record = ("DJIA", 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.72)
# symbol, year, month, day, open, high, low, close = record

# if you want to skip open, high and low
symbol, year, month, day, *_, close = record

print(symbol, year, month, day, close)  # DJIA 2018 1 19 26071.72
print("dummy variables", *_)  # dummy variables 25987.35 26071.72 25942.83
