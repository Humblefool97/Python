from random import shuffle
from random import randint

# in operator
result = 'a' in "Hellow Python!"
print(result)

result = 3 in [1, 2, 3]
print(result)

result = 'k1' in {'k1': 1, 'k2': 2}
print(result)

result = 100 in {'k1': 1, 'k2': 2}.values()
print(result)

# min & max in list
some_list = list(range(10, 40, 10))
minimum = min(some_list)
maximum = max(some_list)
print(f'Minimum in {some_list} is {minimum} & maximum is {maximum}')

shuffle(some_list)

print(some_list)

print(f'Print a number from 0 to 10 0: {randint(0, 100)}')
