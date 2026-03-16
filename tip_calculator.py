# tip_calculator.py

bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter tip percentage: "))

tip = bill * tip_percent / 100
total = bill + tip

print(f"Tip: {tip}")
print(f"Total bill: {total}")