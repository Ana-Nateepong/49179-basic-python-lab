n = int(input())#recieve input
numbers = []#create list
for i in range(n):#put n in list
    num = int(input())
    numbers.append(num)
count = 0
for num in numbers:#see if the number is greater than 50 or not
    if num > 50:
        count += 1
print("จำนวนที่มากกว่า 50:", count)