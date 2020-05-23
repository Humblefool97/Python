from random import randint

# Ask user to input something
name = input('\t===========Hey! whats your name?==========\n\t')
age = input('\t============and your age?==================\n\t')
print(f'Good luck {name}, you gonna die when you are {randint(int(age),100)}')
