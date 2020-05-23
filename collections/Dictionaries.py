# declare and initialize a dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}
print(d)

# Retrieving
print(f"value of k1 is = {d['k1']}")

# Cn hold varied data types
d = {'k1': 123, 'k2': ['a', 'b', 'c'], 'k3': {'j1': "Some value"}}
print(f"value of k2 is {d['k2']} & j1 is {d['k3']['j1']}")

# Return all keys & values
print(f' Keys : {d.keys()} & values are {d.values()}')

# another type of key
e = {123.2: 1}
print(e[123.2])