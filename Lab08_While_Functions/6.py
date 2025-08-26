while True:
    print("1. บวกเลขสองจำนวน\n2. ลบเลขสองจำนวน\n3. คูณเลขสองจำนวน\n4. ออก")
    c = input()
    if c == "4":
        print("จบโปรแกรม")
        break
    a = int(input())
    b = int(input())
    if c == "1": print("ผลลัพธ์:", a + b)
    elif c == "2": print("ผลลัพธ์:", a - b)
    elif c == "3": print("ผลลัพธ์:", a * b)
