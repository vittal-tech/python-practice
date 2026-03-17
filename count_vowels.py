sentence = input("enter a sentnce:")
vowels = "aeiouAEIOU"
count = 0 
for char in sentence :
    if char in vowels:
        count += 1
print("number of vowels:",count)