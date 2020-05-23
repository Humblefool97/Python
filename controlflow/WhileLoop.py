# Simple one
x = 0
while x < 5:
    print(f'value of x is {x}')
    x += 1
else:
    print("X is not less than 5")

# pass
for item in [1, 2, 3]:
    # some comment
    pass
print("After pass")

# continue
for item in [1, 2, 3]:
    if item == 1:
        continue
    print(item)
