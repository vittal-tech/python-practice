import random

print("welcome to the number guessing game!")
print(" i am thinking of a number between 1 to 20")

number = random.randint(1 ,20)

guess = int(input("take a guess:"))

if guess == number :
    print("wow you guessd it right!")
elif guess < number :
    print("too low! try again next time")
else :
    print("too high! try again next time")

print("the number was :" , number)
