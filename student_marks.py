# student marks program

marks = []

for i in range(3) :
    m = int(input(f"Enter mark {i+1} :"))
    marks.append(m)

total = sum(marks)
student = {
    "marks" : marks,
    "total" : total
}

print("marks:" , student["marks"])
print("total:" , student["total"])

print(type(marks))