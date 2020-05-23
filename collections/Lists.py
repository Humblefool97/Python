# declare and initialize a list
my_list = [1, 2, 3]
print(my_list)

# declare & initialize a list with multiple types
my_list = ['STRING', 100, 223.3]
print(f'my_list is {my_list} is of length {len(my_list)}')

# indexing is same as in string
new_list = my_list[2:]
print(new_list)

# concatenating lists
another_list = [23, 456]
new_list = new_list + another_list
print(new_list)

# Add new element to the end
another_list.append('END GAME')
print(another_list)

# Removing the last element
print(f'Removing the last element is {another_list.pop(-1)}')

# Sorting the unsorted list
unsorted_list = [111, 2, 3333]
unsorted_list.sort()
print(f'Sorted list : {unsorted_list}')

# Reversing the list
unsorted_list.reverse()
print(another_list)
