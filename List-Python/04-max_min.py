n = int(input())#recieve input
numbers = []#create a list
for i in range(n):#recieve n and put it in a list
    num = int(input())
    numbers.append(num)
max_num = max(numbers)#find the greatest and the least number from the list
min_num = min(numbers)
print("มากที่สุด:", max_num)
print("น้อยที่สุด:", min_num)