# importing the string and random modules
import string
import random

# defining the characters that can be used in the password
all_characters = string.ascii_letters + string.digits + string.punctuation

# asking the user for the desired length of the password
length = int(input("Enter the length of the password: "))

# checking if the length is at least 8 characters
if length < 8:
    print("Password length must be at least 8 characters.")
    exit()

# generating a password using randomly chosen characters
# using a for loop and range(length)
password = ''
for i in range(length):
    password += random.choice(all_characters)

# displaying the generated password to the user
print("Your password is:", password)
