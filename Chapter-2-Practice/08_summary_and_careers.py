bill = float(input())
tip = float(input())
people = int(input())
total = bill + ((bill * tip) / 100)
amount = round(total / people, 2)
print(amount)