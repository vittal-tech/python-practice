import random
import string

length = int(input("enter your password length:"))

print("1 - letters only")
print("2 - letters + numbers ")
print("3 - letters + numbers + punctuation")

choice = int(input("enter your choice:"))

if choice == 1 :
    characters = string.ascii_letters

elif choice == 2 :
    chracters = string.ascii_letters + string.digits

elif choice == 3 :
    chracters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("passwrd generated:" , password)
