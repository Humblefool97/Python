# Range function
for num in range(10):
    print(num)

# Create a list using range()
some_list = list(range(0, 10, 2))
print(some_list)

# iterate using indexing
some_word = "Hello Python"
for item in enumerate(some_word):
    print(item)
for (index, value) in enumerate(some_word):
    print(f'value of @ index {index} is {value} ')

# Zip: limit is exclusive
list1 = list(range(1, 3))
list2 = list(range(4, 6))
list3 = list(range(7, 10))

for item in zip(list1, list2, list3):
    print(item)
