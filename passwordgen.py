import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

length = input('How many characters does your password need to be? ')
length = int(length)
password = ''
for c in range(length):
    password += random.choice(chars)
print(password)
