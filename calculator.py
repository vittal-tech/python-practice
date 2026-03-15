num1 = int(input("enter first number :"))
num2 = int(input("enter second number:"))
print("1 . add")
print("2 . subtractin")
print("3 . multiplication")
print("4 .division")
choice = int(input("choose operation (1-4):"))
if choice == 1 :
    print("answer:", num1+num2)
elif choice == 2:
    print("answer:",num1-num2)
elif choice == 3 : 
    print("answer:",num1*num2)
elif choice == 4 :
    print("answer:", num1/num2)
else : 
    print("invalid choice")