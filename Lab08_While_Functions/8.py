import random
secret = random.randint(1, 20)
count = 0
while True:
    g = int(input())
    count += 1
    if g > secret: print("มากไป")
    elif g < secret: print("น้อยไป")
    else:
        print(f"ถูกต้อง! คุณทายทั้งหมด {count} ครั้ง")
        break
