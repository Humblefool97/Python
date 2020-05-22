a = "Hello world \n"
print(a * 10)

a = a + "It's a beautiful day"
print(a)

# convert to upper case
a = a.upper()
print(a)

# split
a = a.split(" ")
print(a)

# string formatting
print("Something can be inserted {}".format("here"))

# string formatting using index
print("Something can be inserted {2} {1} {0}".format("index0", "index1", "index2"))

# string formatting using vars
print("Something can be inserted {i} {j} {k}".format(i="index0", j="index1", k="index2"))

# formatting floating point precision
floating = 100 / 777
print("The value of floating is {t:1.3f}".format(t=floating))

# formatting using fString
print(f'The value of floating is {floating:1.3f}')

# formatting using fString for multiple vars
name = 'sam'
age = 25
print(f'{name} is {age} years old')
