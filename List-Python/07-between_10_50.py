n = int(input())#recieve input
numbers = []#create list
result = []
for i in range(n):#put n in list
    num = int(input())
    numbers.append(num)
for num in numbers:#see if the number in list is betweem 10 an 50
    if 10 <= num <= 50:
        result.append(num)
print(result)