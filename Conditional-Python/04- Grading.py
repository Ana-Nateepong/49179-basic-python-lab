grade1 = int(input())
grade2 = int(input())
grade3 = int(input())
total = grade1 + grade2 + grade3

if (80 <= total <= 100):
    print("A")
elif (75 <= total <= 79):
    print("B+")
elif (70 <= total <= 74):
    print("B")
elif (65 <= total <= 69):
    print("C+")
elif (60 <= total <= 64):
    print("C")
elif (55 <= total <= 59):
    print("D+")
elif (50 <= total <= 54):
    print("D")
else:
    print("F")
