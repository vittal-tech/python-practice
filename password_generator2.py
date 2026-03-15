import random
import string

length = int(input("enter your password length (max 20):"))

if length > 20 :
    print("password too long! setting length to 20.")
    length = 20

characters  = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("your password is :" , password)
    
