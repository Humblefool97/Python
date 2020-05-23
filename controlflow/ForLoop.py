# iterate through an iterable
mylist = [1, 2, 3, 4, 5]
for item in mylist:
    print(item)

# print seperate even numbers from odd
for item in mylist:
    # Check if even
    if item % 2 == 0:
        print(f'{item} is even')
    else:
        print(f'{item} is odd')

# maintain indentation
list_sum = 0
for item in mylist:
    # Add numbers
    list_sum = list_sum + item
print(list_sum)

# It will run for len times
for _ in 'Hellow world':
    print('cool')
# Use the same for tuples
tuple_list = [(1, 2), (3, 4), (5, 6)]
for (a, b) in tuple_list:
    print(f' a is {a}')
    print(f' b is {b}')

# Dictionaries
d = {'k1': 1, 'k2': 2, 'k3': 3}
for (key, value) in d.items():
    print(f'Key is {key} Value is {value}')
